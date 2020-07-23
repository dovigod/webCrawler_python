
from indeed import get_jobs as Indeed_jobs
from SOF import get_jobs as SOF_jobs
from save import save_to_file as save


def get_jobs(word):
    Indeed = Indeed_jobs(word)
    ##stackOverFlow = SOF_jobs(word)
    jobs = Indeed
    return jobs