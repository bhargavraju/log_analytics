import unittest
import analytics.time_analysis as ta
from collections import defaultdict


class TestTimeAnalysis(unittest.TestCase):

    def test_time_analysis_empty_dict(self):
        url_dict = defaultdict(dict)
        time_analysis = ta.get_time_analysis(url_dict)
        self.assertEqual(time_analysis, [])

    def test_time_analysis_non_empty_dict(self):
        url_dict = {"/book/{id}": {"POST": [10, 20, 30]}}
        time_analysis = ta.get_time_analysis(url_dict)
        self.assertEqual(time_analysis, [("POST", "/book/{id}", 10, 30, 20.0)])
