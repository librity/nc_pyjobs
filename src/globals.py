def initialize():
  init_debug()
  init_scrapes_path()


def init_debug():
  global DEBUG
  DEBUG = True


def init_scrapes_path():
  global scrapes_path
  scrapes_path = "./scrapes"
