from requests import get
from bs4 import BeautifulSoup


from globals import DEFAULT_HEADERS, QUICK
from so import build_url


def get_pagination_links(url):
  so_req = get(url)

  soup = BeautifulSoup(so_req.text, "html.parser")
  pagination = soup.find("div", {"class": "s-pagination"})
  pagination_links = pagination.find_all('a')

  return pagination_links


def extract_page_numbers(pagination_links):
  page_numbers = []

  for link in pagination_links:
    page_str = link.text

    try:
      page_number = int(page_str)
      page_numbers.append(page_number)

    except:
      continue

  return page_numbers


def get_last_page(query):
  if QUICK:
    return 1

  url = build_url(query, 1)
  pagination_links = get_pagination_links(url)
  page_numbers = extract_page_numbers(pagination_links)

  last_page = max(page_numbers)
  return last_page
