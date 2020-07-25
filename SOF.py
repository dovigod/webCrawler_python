import requests
from bs4 import BeautifulSoup



i=0

        
def getSOFhtml(URL):
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


def extractJobInfo(LPage , URL):

    Information = []
    i=0
    for page in range(LPage):
        ##https://stackoverflow.com/jobs/412456/
       
        raw_data = requests.get(f'{URL}&pg={page+1}')
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
        
    ###find_all (~~~ recursive == false)  ==> 1층에 있는것만 끓어옴
    ### 리스트에 오직 값이 2개!! 만있을때  company, location = 
    
    return Information


def get_jobs(word):
    url = f'https://stackoverflow.com/jobs?q={word}'
    tmp_SOF_html = getSOFhtml(url)
    last_page = getLastPage(tmp_SOF_html)
    jobs = extractJobInfo(last_page , url)
    
    return jobs

