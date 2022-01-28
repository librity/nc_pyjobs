import globals


from indeed_scraper import scrape as scrape_indeed


def main():
  globals.initialize()

  query = "python"

  indeed_jobs = scrape_indeed(query)
  print(indeed_jobs)


if __name__ == "__main__":
  main()
