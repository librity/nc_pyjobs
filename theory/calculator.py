# python3 theory/calculator.py

def add(a, b):
  return validate_and_eval(a, b, "+")


def subtract(a, b):
  return validate_and_eval(a, b, "-")


def multiply(a, b):
  return validate_and_eval(a, b, "*")


def divide(a, b):
  return validate_and_eval(a, b, "/")


def power(a, b):
  return validate_and_eval(a, b, "**")


def remainder(a, b):
  return validate_and_eval(a, b, "%")


def negate(x):
  if not int_or_float(x):
    return None

  return -x


def validate_and_eval(a, b, operation):
  if not valid_params(a, b):
    return None

  return eval(f"{a} {operation} {b}")


def valid_params(a, b):
  if not int_or_float(a):
    return False
  if not int_or_float(b):
    return False

  return True


def int_or_float(number):
  if type(number) == int or type(number) == float:
    return True

  return False


print(add(1, 2))
print(add("1", 2))
print(add(1, "2"))
print(add("1", "2"))


print(subtract(42, 23))
print(multiply(42, 4))
print(divide(42, 2))
print(power(42, 2))
print(remainder(42, 3))
print(negate(42))
