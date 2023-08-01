from job_center.domain import Job, JobRequirements
from job_center.job_store import JobStore


class IndeedIngestor:
    def __init__(self, job_store: JobStore):
        self.base_url = 'https://www.indeed.com/jobs'
        self.job_store = job_store

    def construct_url(self, what, where):
        """TO DO: convert space to + and commas to %2C"""
        return f'{self.base_url}?q={what}&l={where}'

    def ingest(self, what, where):
        """get what job descriptors - title, tools, programing lang etc.
        and get where - location of job like remote or San Fran.
        build the URL with these filters
        """
        url = construct_url(what, where)
