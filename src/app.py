from flask import Flask


app = Flask("pyjobs")


@app.route("/")
def hello():
  return "<p>Howdy folks!</p>"
