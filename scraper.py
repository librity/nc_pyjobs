from indeed_scraper import scrape as scrape_indeed
from so_scraper import scrape as scrape_stack_overflow
from save_to_csv import save_to_csv


def scrape(query):
  indeed_jobs = scrape_indeed(query)
  so_jobs = scrape_stack_overflow(query)

  return indeed_jobs + so_jobs


def build_prefix(query):
  return f"{query}_jobs"


def scrape_to_csv(query):
  jobs = scrape(query)
  prefix = build_prefix(query)

  save_to_csv(prefix, jobs)
