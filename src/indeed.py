BASE_URL = "https://www.indeed.com"
LIMIT = 50


def build_url(query, start):
  return f"{BASE_URL}/jobs?q={query}&start={start}&limit={LIMIT}"
