from csv import DictWriter


from utils import now
from debug import log_debug


SCRAPES_PATH = "./scrapes"


def build_filepath(prefix):
  return f"{SCRAPES_PATH}/{prefix}_{now()}.csv"


def save_to_csv(prefix, jobs):
  keys = jobs[0].keys()
  filepath = build_filepath(prefix)

  with open(filepath, 'w', newline='') as output_file:
    dict_writer = DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(jobs)

  log_debug(f"💾 Saved scrape results to {filepath}")
  return filepath
