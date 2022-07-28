# python3 theory/oop_2.py


class Car():
  def __init__(self, **kwargs):
    self.brand = kwargs.get("brand", None)
    self.model = kwargs.get("model", None)
    self.color = kwargs.get("color", "black")
    self.wheels = kwargs.get("wheels", 4)
    self.windows = kwargs.get("windows", 4)
    self.doors = kwargs.get("doors", 4)
    self.seats = kwargs.get("seats", 4)

  def __str__(self):
    return f"""== Car ==
brand: {self.brand}
model: {self.model}
color: {self.color}
wheels: {self.wheels}
windows: {self.windows}
doors: {self.doors}
seats: {self.seats}
"""

  def start(self):
    print("vroom vrooooom!")


print(dir(Car))
print()

porsche = Car(color="white", brand="Porsche", model="Cayenne")
print(porsche)

ferrari = Car(
    color="red",
    doors=2,
    seats=2,
    windows=2,
    brand="Ferrari",
    model="Stradale",
)
print(ferrari)
ferrari.start()
