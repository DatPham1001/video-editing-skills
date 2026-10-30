"""Exact-duplicate planning tests using temporary synthetic bytes, never real media."""
from pathlib import Path
from tempfile import TemporaryDirectory
import json, unittest
from plan_duplicates import plan_duplicates


class DuplicatePlanTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name); (self.root / '_catalog').mkdir()
        self.old = self.root / 'z-indexed.JPG'; self.old.write_bytes(b'identical-content')
        self.copy = self.root / 'a-copy.JPG'; self.copy.write_bytes(self.old.read_bytes())
        self.checkpoint = self.root / '_catalog/checkpoint.json'
        self.checkpoint.write_text(json.dumps({'items': [{'id': 'MEDIA-001', 'current_path': str(self.old)}]}), encoding='utf-8')

    def test_indexed_file_is_keeper(self):
        result = plan_duplicates(self.root)
        self.assertEqual(result['duplicate_files'], 1)
        self.assertEqual(result['groups'][0]['keeper'], str(self.old))
        self.assertEqual(result['groups'][0]['duplicates'][0]['path'], str(self.copy))

    def test_equal_size_different_bytes_are_not_duplicates(self):
        self.copy.write_bytes(b'X' * len(self.old.read_bytes()))
        self.assertEqual(plan_duplicates(self.root)['groups'], [])

    def test_quarantine_is_excluded(self):
        folder = self.root / '_duplicates/run'; folder.mkdir(parents=True)
        (folder / 'third.JPG').write_bytes(self.old.read_bytes())
        self.assertEqual(plan_duplicates(self.root)['duplicate_files'], 1)

    def test_plan_does_not_mutate_media_or_checkpoint(self):
        before = {p: p.read_bytes() for p in [self.old, self.copy, self.checkpoint]}
        result = plan_duplicates(self.root)
        self.assertEqual((result['files_moved'], result['files_deleted']), (0, 0))
        for p, content in before.items(): self.assertEqual(p.read_bytes(), content)

    def test_three_identical_files_leave_one_keeper(self):
        (self.root / 'third.PNG').write_bytes(self.old.read_bytes())
        result = plan_duplicates(self.root)
        self.assertEqual(result['duplicate_files'], 2)
        self.assertEqual(result['bytes_removable_from_active_set'], 2 * self.old.stat().st_size)


if __name__ == '__main__': unittest.main()
