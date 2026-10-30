"""Read-only exact-duplicate plan. Never moves/deletes files or edits catalog/checkpoint."""
from pathlib import Path
import argparse, collections, json
from plan_update import EXTENSIONS, file_hash, path_key


def plan_duplicates(folder):
    root = Path(folder).resolve()
    indexed_paths = set()
    for name in ['checkpoint.json', 'catalog.json']:
        f = root / name if (root / name).is_file() else root / '_catalog' / name
        if f.is_file():
            payload = json.loads(f.read_text(encoding='utf-8-sig'))
            for row in payload if isinstance(payload, list) else payload.get('items', []):
                if row.get('current_path'):
                    indexed_paths.add(path_key(row['current_path'], root))
    by_size, errors = collections.defaultdict(list), []
    for f in sorted(root.rglob('*')):
        if any(p in {'_catalog', '_duplicates'} for p in f.relative_to(root).parts):
            continue
        if not f.is_file() or f.is_symlink() or f.suffix.lower() not in EXTENSIONS:
            continue
        # A junction/reparse directory must not redirect a candidate outside this root.
        if not f.resolve().is_relative_to(root):
            errors.append({'path': str(f), 'error': 'resolved_outside_media_root'})
            continue
        if any(getattr(p, 'is_junction', lambda: False)() or p.is_symlink() for p in f.parents if p != root and p.is_relative_to(root)):
            errors.append({'path': str(f), 'error': 'symlink_or_junction_parent'})
            continue
        try:
            by_size[f.stat().st_size].append(f)
        except OSError as e:
            errors.append({'path': str(f), 'error': str(e)})
    groups = []
    for size, files in by_size.items():
        if len(files) < 2:
            continue
        by_hash = collections.defaultdict(list)
        for f in files:
            try:
                by_hash[file_hash(f)].append(f)
            except OSError as e:
                errors.append({'path': str(f), 'error': str(e)})
        for sha, duplicates in by_hash.items():
            if len(duplicates) < 2:
                continue
            ranked = sorted(duplicates, key=lambda f: (path_key(f, root) not in indexed_paths, str(f).casefold()))
            groups.append({'sha256': sha, 'bytes_per_file': size, 'keeper': str(ranked[0]),
                'keeper_reason': 'indexed_current_path' if path_key(ranked[0], root) in indexed_paths else 'deterministic_path_order',
                'duplicates': [{'path': str(f), 'indexed_path': path_key(f, root) in indexed_paths,
                                'next_step': 'check_links_then_quarantine_if_cleanup_authorized'} for f in ranked[1:]],
                'recheck_hash_before_move': True})
    return {'folder': str(root), 'mode': 'plan_only', 'files_moved': 0, 'files_deleted': 0,
            'groups': groups, 'errors': errors,
            'duplicate_files': sum(len(g['duplicates']) for g in groups),
            'bytes_removable_from_active_set': sum(g['bytes_per_file'] * len(g['duplicates']) for g in groups),
            'note': 'Quarantine keeps disk usage; inspect links and journal before any authorized move.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folder', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    if not args.folder.is_dir():
        parser.error('Media folder does not exist.')
    result = plan_duplicates(args.folder)
    if args.report:
        protected = {(base / n).resolve() for base in [args.folder, args.folder / '_catalog'] for n in ['checkpoint.json', 'catalog.json', 'path-aliases.json']}
        if args.report.suffix.lower() != '.json' or args.report.resolve() in protected:
            parser.error('Use a separate JSON report; never overwrite catalog/checkpoint/aliases.')
        args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
