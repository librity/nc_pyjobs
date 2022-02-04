from flask import Flask, render_template, request, redirect


import globals
from scraper import scrape


app = Flask("pyjobs")


@app.route("/")
def home():
  return render_template("home.html")


@app.route("/scrapes")
def scrapes():
  query = request.args.get("query")
  if query is "":
    return redirect("/")
  if query is None:
    return redirect("/")

  query = query.lower()
  cached_jobs = globals.jobs_cache.get(query)
  if cached_jobs:
    job_count = len(cached_jobs)
    return render_template("scrapes.html", query=query, jobs=cached_jobs, job_count=job_count)

  scraped_jobs = scrape(query)
  globals.jobs_cache[query] = scraped_jobs
  job_count = len(scraped_jobs)
  return render_template("scrapes.html", query=query, jobs=scraped_jobs, job_count=job_count)


@app.route("/greet/<name>")
def potato(name):
  return f"Hello {name}! How you doing?"
