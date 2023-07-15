class JobRequirements:
    def __init__(self, education='', experience=0, tools=''):
        self.education = education
        self.experience = experience
        self.tools = tools


class Job:
    def __init__(self, title, requirements, location='', salary=0, desc=''):
        assert isinstance(title, str)
        self.title = title
        self.requirements = requirements
        self.location = location
        self.salary = salary
        self.desc = desc

    def __repr__(self):
        return f'title: {self.title}\n' \
               f'salary: {self.salary}\n'

    @property
    def normalize_title(self):
        return self.title.lower().strip()


if __name__ == '__main__':
    jr = JobRequirements()
    job = Job('Data Scientist', jr)
    print(job)
