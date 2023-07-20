from job_store import Education
from util import normalize_title


class JobRequirements:
    def __init__(self, education='', experience=0, tools=''):
        self.raw_education = education
        self.experience = experience
        self.tools = tools

    @property
    def education(self) -> Education:
        ed = self.raw_education.lower()
        if ed in ("hs", "high school", "high-school"):
            return Education.HIGH_SCHOOL
        if ed in ("ba", "bs", "bachelor's", "bachelors", "b.s.", "b.a."):
            return Education.BACHELORS
        if ed in ("ma", "masters", "m.a."):
            return Education.MASTERS
        if ed in ("j.d.", "jd", "phd", "ph.d", "md", "doctorate"):
            return Education.DOCTORATE


class Job:
    def __init__(self, title='', requirements='', location='', salary=0, desc='', company=''):
        assert isinstance(title, str)
        assert isinstance(requirements, JobRequirements)
        self.raw_title = titla
        self.salary = salary
        self.desc = desc

    def __repr__(self):
        return f'title: {self.raw_title}\n' \
               f'salary: {self.salary}\n'

    @property
    def normalized_title(self):
        return normalize_title(self.raw_title)


if __name__ == '__main__':
    jr = JobRequirements()
    job = Job('Data Scientist', jr)
    print(job)
