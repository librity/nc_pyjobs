# SOURCE: https://nomadcoders.co/python-for-beginners/lectures/120/comments/33565

import requests
from bs4 import BeautifulSoup

spans = []


def parsing_proc(result_val):
  indeed_soup = BeautifulSoup(result_val.text, "html.parser")

  pagination = indeed_soup.find("ul", {"class": "pagination-list"})

  pages = pagination.find_all('a')

  temp_spans = []

  for page in pages:
    temp_spans.append(page.find("span"))
    if len(str(temp_spans[0])) == 182:
      spans.extend(temp_spans[3:-1])
      pass
    else:
      spans.extend(temp_spans[:-1])


indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
parsing_proc(indeed_result)

for i in range(200, 901, 100):
  indeed_result = requests.get(
      f"https://www.indeed.com/jobs?q=python&limit=50&start={i}")
  parsing_proc(indeed_result)

print(spans)
