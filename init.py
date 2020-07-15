from indeed import extractIndeedPages
from indeed import extractIndeedJobs



indeed_extract = extractIndeedPages()

jobs=extractIndeedJobs(indeed_extract)


print(jobs)
