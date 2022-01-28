import globals


from indeed_pagination import get_last_page


if __name__ == "__main__":
  globals.initialize()
  print(get_last_page("python", 900))
