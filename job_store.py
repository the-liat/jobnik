from jobnik import Job, JobRequirements


class JobStore:
    def __init__(self):
        self.jobs = []

    def add_job(self, job):
        assert isinstance(job, Job)
        self.jobs.append(job)

    def lookup(self, title):
        return [job for job in self.jobs if title.lower().strip() in job.normalize_title]


if __name__ == '__main__':
    jr = JobRequirements()
    job1 = Job('Data Scientist', jr)
    job2 = Job('Data Manager', jr, salary=112000)
    js = JobStore()
    js.add_job(job1)
    js.add_job(job2)
    jobs = js.lookup('data ')
    print(jobs)
    #print(f'{job1}{job2}')