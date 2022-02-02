from requests import get
from bs4 import BeautifulSoup


import globals
from indeed import build_url


def get_pagination_links(url):
  indeed_req = get(url, headers=globals.DEFAULT_HEADERS)

  soup = BeautifulSoup(indeed_req.text, "html.parser")
  pagination = soup.find("ul", {"class": "pagination-list"})
  pagination_links = pagination.find_all('a')

  return pagination_links


def extract_page_numbers(pagination_links):
  page_numbers = []

  for link in pagination_links:
    page_str = link.text
    if page_str == '':
      continue

    try:
      page_number = int(page_str)
      page_numbers.append(page_number)

    except:
      print(f"Couldn't parse page number from: \"{link}\"")
      continue

  return page_numbers


def get_last_page(query, start):
  url = build_url(query, start)
  pagination_links = get_pagination_links(url)
  page_numbers = extract_page_numbers(pagination_links)

  last_page = max(page_numbers)
  return last_page


def get_last_page_from_sample(query):
  last_pages = []

  for sample in range(0, 1101, 100):
    sample_result = get_last_page(query, sample)
    last_pages.append(sample_result)

  last_page = max(last_pages)
  return last_page
