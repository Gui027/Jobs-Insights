from src.jobs import read


def get_unique_job_types(path):
    jobs_dict = read(path)
    jobs_types = set()

    for job in jobs_dict:
        jobs_types.add(job["job_type"])

    return jobs_types


def filter_by_job_type(jobs, job_type):
    filter_jobs = list()

    for job in jobs:
        if job["job_type"] == job_type:
            filter_jobs.append(job)

    return filter_jobs


def get_unique_industries(path):
    jobs_dict = read(path)
    jobs_industries = set()

    for job in jobs_dict:
        if job["industry"] != '':
            jobs_industries.add(job["industry"])
        # jobs_industries_empty_values = filter(None, jobs_industries)
    return jobs_industries


def filter_by_industry(jobs, industry):
    filter_industry = list()

    for job in jobs:
        if job["industry"] == industry:
            filter_industry.append(job)
    return filter_industry


def get_max_salary(path):
    jobs_dict = read(path)
    jobs_max_salary = list()

    for job in jobs_dict:
        if job["max_salary"] != "" and job["max_salary"].isdigit():
            jobs_max_salary.append(int(job["max_salary"]))
    print(jobs_max_salary)
    max_result = max(jobs_max_salary)
    return max_result


def get_min_salary(path):
    jobs_dict = read(path)
    jobs_min_salary = list()

    for job in jobs_dict:
        if job["min_salary"] != "" and job["min_salary"].isdigit():
            jobs_min_salary.append(int(job["min_salary"]))

    min_result = min(jobs_min_salary)
    return min_result


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
