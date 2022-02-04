def initialize():
  init_debug()
  init_quick()
  init_scrapes_path()
  init_request_headers()
  init_jobs_cache()


def init_debug():
  global DEBUG
  DEBUG = True


def init_quick():
  global QUICK
  QUICK = True


def init_scrapes_path():
  global SCRAPES_PATH
  SCRAPES_PATH = "./scrapes"


def init_request_headers():
  global DEFAULT_HEADERS
  DEFAULT_HEADERS = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
  }


def init_jobs_cache():
  global jobs_cache
  jobs_cache = {}
