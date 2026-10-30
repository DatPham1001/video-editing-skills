"""Read-only SHA-256 delta planner. Does not analyse media or write a checkpoint."""
from pathlib import Path
import argparse, collections, hashlib, json, os

EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.bmp', '.tif', '.tiff', '.heic', '.heif', '.avif', '.mp4', '.mov', '.m4v', '.mkv', '.webm', '.avi', '.mts', '.m2ts'}


def file_hash(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def path_key(raw, root):
    p = Path(raw)
    if not p.is_absolute():
        p = root / p
    return os.path.normcase(str(p.resolve()))


def plan(folder, checkpoint_path=None):
    root = Path(folder).resolve()
    checkpoint_path = Path(checkpoint_path) if checkpoint_path else (root / 'checkpoint.json' if (root / 'checkpoint.json').is_file() else root / '_catalog' / 'checkpoint.json')
    checkpoint = json.loads(checkpoint_path.read_text(encoding='utf-8-sig')) if checkpoint_path.is_file() else {'items': []}
    old = checkpoint.get('items', [])
    by_hash, by_path = collections.defaultdict(list), collections.defaultdict(list)
    for item in old:
        if item.get('sha256'):
            by_hash[item['sha256']].append(item)
        if item.get('current_path'):
            by_path[path_key(item['current_path'], root)].append(item)
    rows, seen, pending = [], set(), []
    for f in sorted(root.rglob('*')):
        if any(part in {'_catalog', '_duplicates'} for part in f.relative_to(root).parts) or not f.is_file() or f.is_symlink() or f.suffix.lower() not in EXTENSIONS:
            continue
        row = {'file': str(f), 'file_name': f.name}
        try:
            row['sha256'] = file_hash(f)
        except OSError as error:
            row.update(action='read_error', error=str(error), analyse=False)
            rows.append(row)
            continue
        matched = by_hash.get(row['sha256'], [])
        if matched:
            seen.update(x['id'] for x in matched)
            row.update(action='skip_reuse', existing_ids=[x['id'] for x in matched], analyse=False,
                       location_metadata_update_only=not any(path_key(x.get('current_path', ''), root) == path_key(f, root) for x in matched))
        else:
            matched = by_path.get(path_key(f, root), [])
            if matched:
                seen.update(x['id'] for x in matched)
                row.update(action='changed_existing_keep_previous', existing_ids=[x['id'] for x in matched], analyse=False)
            else:
                pending.append(row)
        rows.append(row)
    missing = [{'id': x['id'], 'previous_path': x.get('current_path'), 'action': 'missing_from_snapshot', 'delete': False} for x in old if x['id'] not in seen]
    first_new_hash = {}
    for row in pending:
        if row['sha256'] in first_new_hash:
            row.update(action='duplicate_of_new_candidate', duplicate_of=first_new_hash[row['sha256']], analyse=False)
        else:
            first_new_hash[row['sha256']] = row['file']
            row.update(action='new_candidate_needs_identity_check' if missing else 'new_candidate', analyse=False,
                       next_step='Confirm identity, then analyse this new item only; do not mark processed yet.')
    return {'folder': str(root), 'checkpoint': str(checkpoint_path), 'checkpoint_modified': False,
            'summary': dict(collections.Counter(x['action'] for x in rows)), 'files': rows, 'missing': missing}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folder', type=Path)
    parser.add_argument('--checkpoint', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    if not args.folder.is_dir():
        parser.error('Media folder does not exist.')
    result = plan(args.folder, args.checkpoint)
    if args.report:
        protected = {(base / name).resolve() for base in [args.folder, args.folder / '_catalog'] for name in ['checkpoint.json', 'catalog.json', 'path-aliases.json']}
        protected.add(Path(result['checkpoint']).resolve())
        if args.report.resolve() in protected:
            parser.error('Report cannot overwrite the checkpoint.')
        args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'summary': result['summary'], 'missing_records': len(result['missing']), 'checkpoint_modified': False}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
