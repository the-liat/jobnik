from domain import JobRequirements, Job


if __name__ == '__main__':
    jr = JobRequirements()
    job = Job('Data Scientist', jr)
    print(job)
