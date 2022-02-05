from datetime import datetime


def now():
  now = datetime.now()
  now_string = now.strftime("%d-%m-%YT%H:%M:%S")

  return now_string
