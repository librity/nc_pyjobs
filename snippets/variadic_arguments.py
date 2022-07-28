# python3 theory/variadic_arguments.py


def example(a, b, *args, **kwargs):
  print(args)
  print(kwargs)

  return a + b


print(example(1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9,
      money=True, pie="definitely", hello=3.3, SICKO=" mODe"))


def var_plus(*numbers):
  result = 0
  for number in numbers:
    result += number

  return result


print(var_plus(1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9,))
