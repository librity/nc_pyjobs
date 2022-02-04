from flask import Flask, render_template, request, redirect


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
  jobs = scrape(query)

  return render_template("scrapes.html", query=query)


@app.route("/greet/<name>")
def potato(name):
  return f"Hello {name}! How you doing?"
