from requests import get
from bs4 import BeautifulSoup


from debug import log_debug
from indeed_pagination import get_last_page
from indeed import LIMIT, build_url


START = 900


def scrape(query):
  # last_page = get_last_page(query, START)
  # page_numbers = range(0, last_page)
  page_numbers = range(0, 2)
  jobs = []

  for page_number in page_numbers:
    url = build_url(query, LIMIT * page_number)
    log_debug(f"Scrapping jobs from: {url}")

    indeed_req = get(url)

    soup = BeautifulSoup(indeed_req.text, "html.parser")
    page_jobs = soup.find_all("a", {"class": "result"})

    for job in page_jobs:
      title = job.find('h2', {"class": "jobTitle"}).text
      company = job.find('span', {"class": "companyName"}).text
      location = job.find('div', {"class": "companyLocation"}).text

      salary_div = job.find('div', {"class": "salaryOnly"})
      if salary_div == None:
        salary = "n/a"
      else:
        salary = salary_div.text

      link = f"https://www.indeed.com{job.get('href')}"

      pretty_job = {
          "title": title,
          "company": company,
          "location": location,
          "salary": salary,
          "link": link,
      }
      jobs.append(pretty_job)

  return jobs
