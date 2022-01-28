import globals


def log_debug(message):
  if globals.DEBUG:
    print("=== DEBUG ===")
    print(message)
