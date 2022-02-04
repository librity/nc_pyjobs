import globals
from indeed_scraper import scrape_to_csv as scrape_indeed
from so_pagination import get_last_page


def main():
  query = "python"
  # scrape_indeed(query)
  get_last_page(query)


if __name__ == "__main__":
  globals.initialize()
  main()
