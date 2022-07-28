# python3 theory/functions.py


print("=== Python Standard Library ===")
print("42")
print(type("42"))
print(len("42"))
print(abs(-42))
print(int("42"))
print(bool("42"))
print(bool(None))
print(str("42"))
print(str(b'42'))
print(str('std').capitalize())


print()
print("=== User-defined ===")


def say_hello():
  print("hello")


say_hello()
print(say_hello)
print(type(say_hello))


def greet(name="buddy!"):
  print("Hello", name)


greet("Luis")
greet("Nico")
greet()
print(greet())


def plus(a, b):
  return a + b


def minus(a, b=42):
  return a - b


print(plus(21, 21))
print(minus(21, 21))
print(minus(21))
print(plus(b=18, a=24))


def join_line_break(list):
  return "\n".join(str(x) for x in list)


def greet_2(name="pal", age=21, country="Brazil", fav_foods=["pizza", "doritos"]):
  pretty_foods = join_line_break(fav_foods)
  return f"Hello {name}, you are {age} years old!\nYou live in {country} and you love:\n{pretty_foods}\n"


print(greet_2("Luis", 19, "Thayland", [
      "sushi", "chicken nuggets", "whopper", "beer"]))
print(greet_2("Nico", 30))
