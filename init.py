
from indeed import get_jobs as Indeed_jobs
from SOF import get_jobs as SOF_jobs


def get_jobs(word):
    Indeed = Indeed_jobs(word)
    stackOverFlow = SOF_jobs(word)
    jobs = Indeed + stackOverFlow
    return jobs