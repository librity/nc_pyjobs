import imp
from flask import Flask, render_template, request, redirect, send_file


import globals
from scraper import scrape
from save_to_csv import save_to_csv


app = Flask("pyjobs")


@app.route("/example/<name>")
def potato(name):
  return f"Hello {name}! How you doing?"


@app.route("/")
def home():
  return render_template("home.html")


@app.route("/scrapes")
def scrapes():
  query = request.args.get("query")
  if bad_query(query):
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


@app.route("/scrapes/export")
def export_scrape():
  query = request.args.get("query")
  if bad_query(query):
    return redirect("/")
  query = query.lower()

  cached_jobs = globals.jobs_cache.get(query)
  if cached_jobs:
    filepath = save_to_csv(f"{query}_jobs", cached_jobs)
    return send_file(filepath)

  scraped_jobs = scrape(query)
  globals.jobs_cache[query] = scraped_jobs
  filepath = save_to_csv(f"{query}_jobs", cached_jobs)
  return send_file(filepath)


def bad_query(query):
  if query is "":
    return True
  if query is None:
    return True

  return False
