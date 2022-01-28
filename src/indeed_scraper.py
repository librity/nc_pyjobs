from requests import get
from bs4 import BeautifulSoup
from csv import DictWriter

import globals
from utils import now
from indeed_pagination import get_last_page
from indeed import BASE_URL, LIMIT, build_url


START = 900


def get_title(job):
  title_h2 = job.find('h2', {"class": "jobTitle"})
  return title_h2.text


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
      "salary": get_salary(job),
      "link": get_link(job),
  }


def get_page_jobs(query, page_number):
  url = build_url(query, LIMIT * page_number)
  print(f"⛏️  Scrapping jobs from: {url}")

  indeed_req = get(url)

  soup = BeautifulSoup(indeed_req.text, "html.parser")
  page_jobs = soup.find_all("a", {"class": "result"})

  return page_jobs


def scrape(query):
  print(f"🧑‍💻 Scrapping {BASE_URL} for {query} jobs")

  last_page = get_last_page(query, START)
  print(f"🔎 Found {last_page} page(s) of jobs")

  page_numbers = range(0, last_page)
  jobs = []

  for page_number in page_numbers:
    page_jobs = get_page_jobs(query, page_number)

    for job in page_jobs:
      pretty_job = format_job(job)
      jobs.append(pretty_job)

  return jobs


def build_filepath(query):
  return f"{globals.scrapes_path}/indeed_{query}_{now()}.csv"


def scrape_to_csv(query):
  jobs = scrape(query)
  keys = jobs[0].keys()
  filepath = build_filepath(query)

  with open(filepath, 'w', newline='') as output_file:
    dict_writer = DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(jobs)

  print(f"💾 Saved scrape results to {filepath}")
