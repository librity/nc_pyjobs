from globals import DEBUG

def log_debug(message):
  if DEBUG:
    print("=== DEBUG ===")
    print(message)
