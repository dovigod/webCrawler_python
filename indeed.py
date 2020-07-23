import requests
from bs4 import BeautifulSoup ##screen scraping lib
LIMIT = 50
def getLastPage(url):

    INDEED_result = requests.get(url)

    soup = BeautifulSoup(INDEED_result.text, "html.parser")

    pagination = soup.find("div",{"class":"pagination"})


    pages=pagination.find_all('a')
    
    spans = []
    
    for page in pages[:-1]:
        spans.append(int(page.find("span").string))


    MAX_page = spans[-1]
   
    return MAX_page;


def getLocation(html):

    location_series = html.find("span", {"class":"location"})
    if location_series is not None:
        return location_series.string
    else:
        location_series = html.find("div",{"class":"location"})
        return location_series.string

def getSalaryInfo(html):
    if html is not None:
        target = html.find("span").find("span",{"class":"salaryText"})
        return (target.string)[1:]
    
    else:
        return "NO INFO"




def getJobNCompany(result): ## extract jobs
    title = result.find("h2",{"class":"title"}).find("a")["title"]
    title_sjcl =result.find("div",{"class":"sjcl"})
    titles = title_sjcl.find("div").find("span",{"class":"company"})
    title_anchor = titles.find("a",{"class":"turnstileLink"})
    salary_loc = result.find("div",{"class":"salarySnippet"})
    job_id = result["data-jk"]
    APPLY_LINK = f'https://kr.indeed.com/%EC%B1%84%EC%9A%A9%EB%B3%B4%EA%B8%B0?jk={job_id}'
    salary = getSalaryInfo(salary_loc)


    location = getLocation(title_sjcl)
    if title_anchor is None:
        company = str(titles.string)
    else:
        company = str(title_anchor.string)
    
    company =company.strip( )
    return {"title":title , "company":company , "location":location,"url":APPLY_LINK}


def extractIndeedJobs(last_page , INDEED_URL):
    jobs=[]
    for page in range(last_page):
        if page == 15:
            break
        
        result = requests.get(f"{INDEED_URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        manu_result = soup.find_all("div",{"class" :"jobsearch-SerpJobCard"})  ## 표제 section 추출
        for result in manu_result:
            jobs.append(getJobNCompany(result))

    return jobs



def get_jobs(word):
    url = f'https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and={word}&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&radius=25&l=%EC%84%9C%EC%9A%B8+%EA%B0%95%EB%82%A8%EA%B5%AC&fromage=any&limit={LIMIT}&sort=&psf=advsrch&from=advancedsearch'

    Lpage = getLastPage(url)
    jobs=extractIndeedJobs(Lpage , url)
    return jobs

