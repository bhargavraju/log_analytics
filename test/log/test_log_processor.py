import unittest
import log.log_processor as processor


class TestLogProcessor(unittest.TestCase):

    def test_process_log_file(self):
        urls = processor.process_log_file("files/test_log.csv")
        self.assertEqual(urls, {'/book/{id}/return': {'GET': [45]}})

    def test_process_log_file_wrong_path(self):
        self.assertRaises(FileNotFoundError, processor.process_log_file, "wrong_path.csv")
