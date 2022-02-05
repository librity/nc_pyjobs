from requests import get
from bs4 import BeautifulSoup

import globals
from indeed_pagination import get_last_page
from indeed import BASE_URL, LIMIT, build_url
from save_to_csv import save_to_csv
from debug import log_debug

MAX_START = 900


def get_title(job):
  title_h2 = job.find('h2', {"class": "jobTitle"})
  last_span = title_h2.contents[-1]
  title = last_span['title']
  return title


def get_company(job):
  company_span = job.find('span', {"class": "companyName"})
  return company_span.text


def get_location(job):
  location_div = job.find('div', {"class": "companyLocation"})
  return location_div.text


def get_salary(job):
  salary_div = job.find('div', {"class": "salaryOnly"})
  if salary_div == None:
    return "N/A"

  return salary_div.text


def get_link(job):
  endpoint = job.get('href')
  return f"{BASE_URL}{endpoint}"


def format_job(job):
  return {
      "title": get_title(job),
      "company": get_company(job),
      "location": get_location(job),
      "link": get_link(job),
  }


def get_page_jobs(query, page_number):
  url = build_url(query, LIMIT * page_number)
  log_debug(f"⛏️  Scrapping jobs from: {url}")

  indeed_req = get(url, headers=globals.DEFAULT_HEADERS)

  soup = BeautifulSoup(indeed_req.text, "html.parser")
  page_jobs = soup.find_all("a", {"class": "result"})

  return page_jobs


def scrape(query):
  log_debug(f"🧑‍💻 Scrapping {BASE_URL} for {query} jobs")

  last_page = get_last_page(query, MAX_START)
  log_debug(f"🔎 Found {last_page} page(s) of jobs")

  page_numbers = range(0, last_page)
  jobs = []

  for page_number in page_numbers:
    page_jobs = get_page_jobs(query, page_number)

    for job in page_jobs:
      pretty_job = format_job(job)
      jobs.append(pretty_job)

  return jobs


def build_prefix(query):
  return f"indeed_{query}"


def scrape_to_csv(query):
  jobs = scrape(query)
  prefix = build_prefix(query)
  save_to_csv(prefix, jobs)
