# python3 theory/variables.py


print("=== Integers ===")
a_int = 2
print(type(a_int))
b = 3
print(a_int, b)
print(a_int + b)


print()
print("=== Floats ===")
a_float = 2.71828182845904523536028747135266249775724709369995957
print(type(a_float))
print("e:", a_float)


print()
print("=== Strings ===")
a_string = "Hello!"
print(type(a_string))
print(a_string)
name = "Luis"
age = "19"
print("My name is " + name + " and I am " + age + " years old.")
print("My name is", name, "and I am",  age, "years old.")

# from string import Template
# print()
# print("=== Templates ===")
# a_template = Template('My name is ${name} and I am ${age} years old.')
# print(type(a_template))
# greeting = a_template.substitute(name=name, age=age)
# print(greeting)

print()
print("=== Booleans ===")
a_boolean = True
if(a_boolean):
  print(a_boolean)
a_boolean = False
if(a_boolean):
  print(a_boolean)
print(type(a_boolean))


print()
print("=== None ===")
print("Like ruby's nil")
a_none = None
if(a_none):
  print(a_none)
print(type(a_none))
