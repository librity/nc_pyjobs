# python3 theory/oop_1.py


# from pprint import pprint


class Car():
  brand = None
  model = None
  color = None
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

  def inspect(car):
    print("== Car ==")
    print("brand:", car.brand)
    print("model:", car.model)
    print("color:", car.color)
    print("wheels:", car.wheels)
    print("doors:", car.doors)
    print("windows:", car.windows)
    print("seats:", car.seats)
    print("")

  def start(self):
    print("vroom vrooooom!")


print(dir(Car))
print()

porsche = Car()
porsche.color = "white"
porsche.brand = "Porsche"
porsche.model = "Cayenne"
porsche.inspect()
# pprint(porsche)

ferrari = Car()
ferrari.color = "red"
ferrari.doors = 2
ferrari.seats = 2
ferrari.windows = 2
ferrari.brand = "Ferrari"
ferrari.model = "Stradale"
ferrari.inspect()
# pprint(ferrari)
ferrari.start()
