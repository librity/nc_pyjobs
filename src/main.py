import globals


from indeed_pagination import get_last_page


def main():
  globals.initialize()
  print(get_last_page("python", 900))


if __name__ == "__main__":
  main()
