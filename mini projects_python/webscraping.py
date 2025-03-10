from bs4 import BeautifulSoup
import requests
link = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=").text
soup = BeautifulSoup(link, "lxml")
jobs = soup.find_all("li", "clearfix job-bx wht-shd-bx")
unfamiliar_skill = input("enter your unfamiliar skill : ")

for job in jobs:
    date_posted = job.find("span", class_ = "sim-posted").text.strip()
    company_name = job.find("h3", class_ = 'joblist-comp-name').text.strip()
    req_skills = job.find("span", class_ = "srp-skills").text.strip()
    more_info = job.header.h2.a['href']

    if ("few" in date_posted):
        if (unfamiliar_skill not in req_skills):
            print(f"company name : {company_name}")
            print(f"required skills : {req_skills}")
            print(f"date posted : {date_posted}")
            print(f"more info : {more_info}")
            print("\n")


