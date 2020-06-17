import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&pg=2"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_job_info(html):
    title = html.find("h2", {
        "class": "mb4 fc-black-800 fs-body3"
    }).find("a")["title"]
    # 이 방법도 좋긴 한데, 두번째 span 의 class 이름이 다 같다는 보장이 없기 때문에 아래 방법이 더 나은 것 같다.
    # 그렇긴 한데 또 h3 안에 span 이 두개씩 들어있다는 보장 역시 없기 때문에 이에 대한 처리가 필요할 듯 하다.
    company_info = html.find("h3", {"class": "fc-black-700 fs-body1 mb4"})
    # company = company_info.find("span").get_text(strip=True)
    # location = company_info.find("span", {"class": "fc-black-500"}).get_text(strip=True)
    company_info = company_info.get_text(strip=True)

    company_row, location_row = html.find("h3", {
        "class": "fc-black-700 fs-body1 mb4"
    }).find_all(
        "span", recursive=False)
    company_row = company_row.get_text(strip=True)
    location_row = location_row.get_text(strip=True)
    job_id = html["data-jobid"]
    link = f"https://stackoverflow.com/jobs/{job_id}"

    return {
        "title": title,
        "company": company_row,
        "location": location_row,
        "link": link
    }


def get_jobs_info(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping sof page: {page}")
        result = requests.get(f"{URL}&pg={0 + 1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job_info(result)
            jobs.append(job)

    return jobs


def get_jobs_data():
    last_page = get_last_page()
    jobs = get_jobs_info(last_page)
    return jobs
