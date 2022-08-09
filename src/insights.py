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

    if ("min_salary" or "max_salary") not in job:
        raise ValueError("Chave min_salary ou max_salary ausentes")

    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("Chave min_salary ou max_salary não-numéricos")

    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary é maior que max_salary")

    if type(salary) != int:
        raise ValueError("O parâmetro salary não é numérico")

    return salary >= job["min_salary"] and salary <= job["max_salary"]


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
