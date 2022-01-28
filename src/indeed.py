LIMIT = 50


def build_url(query, start):
  return f"https://www.indeed.com/jobs?q={query}&start={start}&limit={LIMIT}"
