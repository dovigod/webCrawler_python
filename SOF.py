import requests
from bs4 import BeautifulSoup

URL = f'https://stackoverflow.com/jobs?'

i=0

        
def getSOFhtml():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    
    return soup

def getPagination(html):
    pagination = html.find("div",{"class":"s-pagination"})
    return pagination



def getLastPage(html):
    pagination = getPagination(html)
    
    pages = pagination.find_all("a")
    pages = pages[-2]
    return int(pages.find("span").get_text(strip = True))
    

def getJobTitle(html):
    title = str(html.find("h2").find("a",{"class":"stretched-link"})['title'])
    return title

def getCompanyName(html):
    company = html.find("h3").find("span").get_text(strip = True)
    return company

def getLocation(html):
    location = html.find("h3").find("span",{"class":"fc-black-500"}).get_text(strip = True)
    return location

def getJobURL(html):
    url_id = html["data-result-id"]
    target = f'https://stackoverflow.com/jobs/{url_id}'
    return target


def extractJobInfo(LPage):

    Information = []
    i=0
    for page in range(LPage):
        ##https://stackoverflow.com/jobs/412456/
        print(f"scrapping page {page+1}")
        raw_data = requests.get(f'{URL}pg={page+1}')
        parsed = BeautifulSoup(raw_data.text,"html.parser")
        job_list = parsed.find("div",{"class":"listResults"})
        job_cell = job_list.find_all("div",{"class":"fl1"})
        job_ID = job_list.find_all("div",{"class":"js-dismiss-overlay-container"})
        



        for jobs in job_cell:
            title = getJobTitle(jobs)
            company = getCompanyName(jobs)
            location = getLocation(jobs)
            Information.append({"title":title , "company":company , "location":location})
            
       

    
        for index in job_ID:
           
            
            Information[i].update({"url": getJobURL(index)})
            ##Information[index] = {"url":url}
            i=i+1
        
        print(Information)

    
    return Information


def get_jobs():
    tmp_SOF_html = getSOFhtml()
    last_page = getLastPage(tmp_SOF_html)
    jobs = extractJobInfo(last_page)
 
    return jobs