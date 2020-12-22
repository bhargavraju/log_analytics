import unittest
import log.url_modifier as modifier


class TestUrlModifier(unittest.TestCase):

    def test_id_replacer_id_in_middle(self):
        self.assertEqual(modifier.id_replacer("/book/147/return"), "/book/{id}/return")

    def test_id_replacer_id_at_end(self):
        self.assertEqual(modifier.id_replacer("/book/2"), "/book/{id}")

    def test_id_replacer_no_id(self):
        self.assertEqual(modifier.id_replacer("/person/all"), "/person/all")
