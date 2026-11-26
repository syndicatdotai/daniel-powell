import copy
import json
import tempfile
import unittest
from pathlib import Path

import archive_summary as summary


class SummaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root/'new-subject').mkdir()
        self.path = 'new-subject/example.md'
        self.text = '# Example\n\nDaniel prepared drawings.\n'
        (self.root/self.path).write_text(self.text, encoding='utf-8')
        self.record = dict(id='topic:example', title='Example', section='new-subject',
                           path=self.path, legacyPaths=['old/example.md'],
                           summary='Daniel prepared drawings for a project.',
                           tags=['drafting', 'project-coordination', 'drawings'], custom='keep')
        summary.stamp(self.record, self.text)
        self.catalog = dict(sections=[dict(key='new-subject', title='New Subject',
                            description='New topics.', index='new-subject/index.md')], records=[self.record])
        (self.root/'SUMMARY.md').write_text(summary.render(self.catalog), encoding='utf-8')

    def test_non_pub_and_new_category(self):
        self.assertEqual(summary.validate(self.root, self.catalog), [])

    def test_content_edit_is_stale_until_review(self):
        text = self.text + '\nThe drawing package was revised.\n'
        (self.root/self.path).write_text(text, encoding='utf-8')
        self.assertTrue(any('stale content hash' in e for e in summary.validate(self.root,self.catalog)))
        summary.stamp(self.record,text)
        self.assertEqual(summary.validate(self.root,self.catalog), [])
        self.assertEqual(self.record['custom'],'keep')

    def test_rename_and_legacy_path(self):
        target='new-subject/renamed.md'
        (self.root/self.path).rename(self.root/target)
        self.record['path']=target
        self.record['legacyPaths'].append(self.path)
        self.assertTrue(any('SUMMARY.md' in e for e in summary.validate(self.root,self.catalog)))
        (self.root/'SUMMARY.md').write_text(summary.render(self.catalog),encoding='utf-8')
        self.assertEqual(summary.validate(self.root,self.catalog),[])

    def test_missing_metadata_and_uncataloged_content(self):
        del self.record['summary']
        (self.root/'new-subject/supplement.md').write_text('# Supplement',encoding='utf-8')
        errors=summary.validate(self.root,self.catalog)
        self.assertTrue(any('summary must' in e for e in errors))
        self.assertTrue(any('Uncataloged' in e for e in errors))

    def test_preflight_can_read_new_content_without_writing(self):
        (self.root/self.path).unlink()
        self.assertEqual(summary.validate(self.root,self.catalog,False,{self.path:self.text}),[])
        self.assertFalse((self.root/self.path).exists())

    def test_summary_approval_fingerprint_changes(self):
        changed=copy.deepcopy(self.record)
        changed['summary']='Daniel revised the drawings.'
        self.assertNotEqual(summary.metadata_fingerprint(changed),summary.metadata_fingerprint(self.record))
        changed=copy.deepcopy(self.record)
        changed['custom']='unrelated'
        self.assertEqual(summary.metadata_fingerprint(changed),summary.metadata_fingerprint(self.record))

    def test_readable_count_and_normalized_hash(self):
        text='# Well-made drawings\n\n[Open details](https://example.com/long/url)\n'
        self.assertEqual(summary.word_count(text),4)
        self.assertEqual(summary.content_hash(text),summary.content_hash(text.replace('\n','\r\n')))

    def test_unsafe_path_rejected(self):
        self.record['path']='../outside.md'
        self.assertTrue(any('escapes archive' in e for e in summary.validate(self.root,self.catalog)))


if __name__=='__main__':
    unittest.main()
