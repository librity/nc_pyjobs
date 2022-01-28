from requests import get
from bs4 import BeautifulSoup
from pprint import pprint

DEBUG = False


def build_url(query, start):
  return f"https://www.indeed.com/jobs?q={query}&start={start}&limit=50"


def get_pagination_links(url):
  indeed_req = get(url)

  soup = BeautifulSoup(indeed_req.text, "html.parser")
  pagination = soup.find("ul", {"class": "pagination-list"})
  pagination_links = pagination.find_all('a')

  return pagination_links


def extract_pagination(pagination_links):
  pagination = []

  for pagination_link in pagination_links:
    pagination_span = pagination_link.find("span")

    if DEBUG:
      pprint(pagination_span)

    if pagination_span.text == '':
      continue

    try:
      pagination_number = int(pagination_span.text)
      pagination.append(pagination_number)

    except:
      if DEBUG:
        print(f"Couldn't parse span: \"{pagination_span}\"")
      continue

  return pagination


def get_last_page(query, start):
  url = build_url(query, start)
  pagination_links = get_pagination_links(url)
  pagination = extract_pagination(pagination_links)
  last_page = max(pagination)

  return last_page
