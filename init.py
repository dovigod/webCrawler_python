
from indeed import get_jobs as Indeed_jobs
from SOF import get_jobs as SOF_jobs
from save import save_to_file as save
stackOverFlow = SOF_jobs()
Indeed = Indeed_jobs()

jobs = stackOverFlow + Indeed

save(jobs)

