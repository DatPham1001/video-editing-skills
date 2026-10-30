"""Synthetic temporary files only; no actual image/video analysis."""
from pathlib import Path
from tempfile import TemporaryDirectory
import hashlib, json, unittest
from plan_update import plan


class DeltaTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name); self.catalog = self.root / '_catalog'; self.catalog.mkdir()
        self.original = self.root / 'old.JPG'; self.original.write_bytes(b'synthetic media bytes')
        self.checkpoint = self.catalog / 'checkpoint.json'
        self.checkpoint.write_text(json.dumps({'items': [{'id': 'MEDIA-001', 'current_path': str(self.original), 'sha256': hashlib.sha256(self.original.read_bytes()).hexdigest()}]}), encoding='utf-8')

    def test_existing_is_reused(self):
        self.assertEqual(plan(self.root)['summary'], {'skip_reuse': 1})

    def test_renamed_file_is_reused(self):
        self.original.rename(self.root / 'renamed.JPG')
        result = plan(self.root)
        self.assertEqual(result['summary'], {'skip_reuse': 1})
        self.assertTrue(result['files'][0]['location_metadata_update_only'])
        self.assertEqual(result['missing'], [])

    def test_new_file_becomes_candidate(self):
        (self.root / 'new.MP4').write_bytes(b'new synthetic bytes')
        self.assertEqual(plan(self.root)['summary']['new_candidate'], 1)

    def test_changed_old_file_is_not_reanalysed(self):
        self.original.write_bytes(b'changed content')
        result = plan(self.root)['files'][0]
        self.assertEqual(result['action'], 'changed_existing_keep_previous')
        self.assertFalse(result['analyse'])

    def test_duplicate_new_files_are_analysed_once(self):
        for name in ['new1.PNG', 'new2.PNG']: (self.root / name).write_bytes(b'new identical bytes')
        result = plan(self.root)['summary']
        self.assertEqual(result['new_candidate'], 1)
        self.assertEqual(result['duplicate_of_new_candidate'], 1)

    def test_missing_and_unmatched_new_requires_identity_review(self):
        self.original.unlink(); (self.root / 'unknown.MP4').write_bytes(b'unknown content')
        result = plan(self.root)
        self.assertEqual(result['summary']['new_candidate_needs_identity_check'], 1)
        self.assertFalse(result['missing'][0]['delete'])

    def test_generated_preview_is_ignored(self):
        (self.catalog / 'preview.PNG').write_bytes(b'generated output')
        self.assertEqual(len(plan(self.root)['files']), 1)

    def test_quarantined_duplicate_is_not_a_new_file(self):
        folder = self.root / '_duplicates' / 'fixture-run'; folder.mkdir(parents=True)
        (folder / 'duplicate.JPG').write_bytes(self.original.read_bytes())
        self.assertEqual(plan(self.root)['summary'], {'skip_reuse': 1})

    def test_checkpoint_is_not_modified(self):
        before = self.checkpoint.read_bytes(); plan(self.root)
        self.assertEqual(before, self.checkpoint.read_bytes())


if __name__ == '__main__': unittest.main()
