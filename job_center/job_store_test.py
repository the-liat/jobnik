import unittest

from domain import Job, JobRequirements
from job_store import JobStore


class JobStoreTest(unittest.TestCase):

    def setUp(self):
        """set up creating an empty job store object, it runs before each test"""
        self.js = JobStore()

    def test_add_job(self):
        """testing that adding a job is stored in the job store object"""
        # create a job (instantiate an object of the Job class)
        jr = JobRequirements(tools='SQL')
        job = Job('Data Manager', jr, 'remote')

        # calling the code under test
        self.js.add_job(job)

        # verify the job was added properly to the job store
        self.assertIn(job, self.js.jobs)
