import unittest
import analytics.frequent_calls as fc
from collections import defaultdict


class TestFrequentCalls(unittest.TestCase):

    def test_most_frequent_calls_empty_dict(self):
        url_dict = defaultdict(dict)
        most_frequent_calls = fc.get_most_frequent_calls(url_dict, 5)
        self.assertEqual(most_frequent_calls, [])

    def test_most_frequent_calls_no_of_distinct_calls_less_than_k(self):
        url_dict = {"/book/{id}": {"POST": [10, 20, 30], "PUT": [10, 13]}}
        most_frequent_calls = fc.get_most_frequent_calls(url_dict, 5)
        self.assertEqual(most_frequent_calls, [("POST", "/book/{id}", 3), ("PUT", "/book/{id}", 2)])

    def test_most_frequent_calls_no_of_distinct_calls_greater_than_k(self):
        url_dict = {"/book/{id}": {"POST": [10, 20, 30], "PUT": [10, 13]}}
        most_frequent_calls = fc.get_most_frequent_calls(url_dict, 1)
        self.assertEqual(most_frequent_calls, [("POST", "/book/{id}", 3)])
