from dataclasses import dataclass
from typing import List

from domain import Job, JobRequirements, Education
from util import normalize_title


@dataclass
class SearchCriteria:
    title: str
    education: Education
    years_of_experience_low: int
    years_of_experience_hi: int
    tools: List[str]
    location: str
    salary_low: int
    salary_hi: int


class JobStore:
    def __init__(self):
        self.jobs = []

    def add_job(self, job):
        assert isinstance(job, Job)
        self.jobs.append(job)

    def lookup_by_title(self, title):
        return [job for job in self.jobs if title.lower().strip() in job.normalized_title]

    def _match(self, job: Job, criteria: SearchCriteria) -> bool:
        """return True if the job matches the criteria, otherwise False"""
        if criteria.title and job.normalized_title != normalize_title(criteria.title):
            return False
        if criteria.education and job.normalized_title != normalize_title(criteria.title):
            return False
        education: Education
        years_of_experience_low: int
        years_of_experience_hi: int
        tools: List[str]
        location: str
        salary_low: int
        salary_hi: int

    def search(self, criteria: SearchCriteria):
        assert isinstance(criteria, SearchCriteria)

        """title: str
        education: Education
        years_of_experience_low: int
        years_of_experience_hi: int
        tools: List[str]
        location: str
        salary_low: int
        salary_hi: int"""


if __name__ == '__main__':
    jr = JobRequirements()
    job1 = Job('Data Scientist', jr)
    job2 = Job('Data Manager', jr, salary=112000)
    js = JobStore()
    js.add_job(job1)
    js.add_job(job2)
    jobs = js.lookup_by_title('data ')
    print(jobs)
    # print(f'{job1}{job2}')
