from requests import get
from bs4 import BeautifulSoup

from globals import DEFAULT_HEADERS
from so_pagination import get_last_page
from so import BASE_URL, build_url
from save_to_csv import save_to_csv
from debug import log_debug


MAX_START = 900


def get_title(job):
  title_a = job.find('a', {"class": "s-link"})
  return title_a['title']


def get_company(job):
  company_and_location = job.find('h3', {"class": "fc-black-700"})
  company_span = company_and_location.find_all("span")[0]

  return company_span.get_text(strip=True)


def get_location(job):
  company_and_location = job.find('h3', {"class": "fc-black-700"})
  location_span = company_and_location.find_all("span")[-1]

  return location_span.get_text(strip=True)


def get_link(job):
  job_id = job['data-result-id']
  return f"{BASE_URL}/jobs/{job_id}"


def format_job(job):
  return {
      "title": get_title(job),
      "company": get_company(job),
      "location": get_location(job),
      "link": get_link(job),
  }


def get_page_jobs(query, page_number):
  url = build_url(query, page_number)
  log_debug(f"⛏️  Scrapping jobs from: {url}")

  indeed_req = get(url)

  soup = BeautifulSoup(indeed_req.text, "html.parser")
  page_jobs = soup.find_all("div", {"class": "-job"})

  return page_jobs


def scrape(query):
  log_debug(f"🧑‍💻 Scrapping {BASE_URL} for {query} jobs")

  last_page = get_last_page(query)
  log_debug(f"🔎 Found {last_page} page(s) of jobs")

  page_numbers = range(1, last_page + 1)
  jobs = []

  for page_number in page_numbers:
    page_jobs = get_page_jobs(query, page_number)

    for job in page_jobs:
      pretty_job = format_job(job)
      jobs.append(pretty_job)

  return jobs


def build_prefix(query):
  return f"stack_overflow_{query}"


def scrape_to_csv(query):
  jobs = scrape(query)
  prefix = build_prefix(query)
  save_to_csv(prefix, jobs)
