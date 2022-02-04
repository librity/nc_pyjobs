import globals
from indeed_scraper import scrape_to_csv as scrape_indeed
from so_scraper import scrape_to_csv as scrape_stack_overflow


def main():
  query = "python"
  scrape_indeed(query)
  scrape_stack_overflow(query)


if __name__ == "__main__":
  globals.initialize()
  main()
