from flask import Flask, render_template, request


app = Flask("pyjobs")


@app.route("/")
def home():
  return render_template("home.html")


@app.route("/scrapes")
def scrapes():
  query = request.args.get("query")

  return render_template("scrapes.html", query=query)


@app.route("/greet/<name>")
def potato(name):
  return f"Hello {name}! How you doing?"
