import requests
from bs4 import BeautifulSoup ##screen scraping lib
LIMIT = 50
INDEED_URL = f'https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&radius=25&l=%EC%84%9C%EC%9A%B8+%EA%B0%95%EB%82%A8%EA%B5%AC&fromage=any&limit={LIMIT}&sort=&psf=advsrch&from=advancedsearch'

INDEED_result = requests.get(INDEED_URL)

def extractIndeedPages():
    soup = BeautifulSoup(INDEED_result.text, "html.parser")

    pagination = soup.find("div",{"class":"pagination"})


    pages=pagination.find_all('a')
    
    spans = []
    
    for page in pages[:-1]:
        spans.append(int(page.find("span").string))


    MAX_page = spans[-1]
    return MAX_page;


def extractIndeedJobs(last_page):
    jobs=[]
    ##for page in range(last_page):
    result = requests.get(f"{INDEED_URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    manu_result = soup.find_all("div",{"class" :"jobsearch-SerpJobCard"})
    for result in manu_result:
        titles = result.find("h2",{"class":"title"}).find("a")["title"]
        print(titles)
    return jobs
    