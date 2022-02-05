BASE_URL = "https://stackoverflow.com"


def build_url(query, page):
  return f"{BASE_URL}/jobs?q={query}&pg={page}"
