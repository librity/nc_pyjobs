import globals
from indeed_scraper import scrape_to_csv as scrape_indeed


def main():
  query = "python"
  scrape_indeed(query)


if __name__ == "__main__":
  globals.initialize()
  main()
