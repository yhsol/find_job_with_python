import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"


def get_last_page():
    results = requests.get(URL)
    soup = BeautifulSoup(results.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page


def extract_job_data(html):
    title = html.find("div", {"class": "title"}).find("a")["title"]

    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company:
      if company_anchor is not None:
          company = str(company_anchor.string)
      else:
          company = str(company.string)
    else:
      company = None
    company = company.strip()

    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]

    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://kr.indeed.com/viewjob?jk={job_id}"
    }

def get_jobs_info(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping indeed page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job_data(result)
            jobs.append(job)
    return jobs

def get_jobs_data():
  last_page = get_last_page()
  jobs = get_jobs_info(last_page)
  return jobs