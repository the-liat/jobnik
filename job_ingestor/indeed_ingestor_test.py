import unittest

from job_center.job_store import JobStore
from job_ingestor.indeed_ingestor import IndeedIngestor


class IndeedIngestorTest(unittest.TestCase):

    def setUp(self):
        """ """
        js = JobStore()
        self.indeed_ing = IndeedIngestor(js)

    def test_construct_url(self):
        """testing that special characters are transformed to base64"""
        what = "lead;science"
        where = "Davis, CA"
        expected_url = "https://www.indeed.com/jobs?q=lead%3Bscience&l=Davis%2C+CA"
        url = self.indeed_ing.construct_url(what, where)
        self.assertEqual(url, expected_url)