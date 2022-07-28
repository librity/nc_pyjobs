# python3 theory/oop_3.py


from time import sleep


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
    return f"""=== Car ===
brand: {self.brand}
model: {self.model}
color: {self.color}
wheels: {self.wheels}
windows: {self.windows}
doors: {self.doors}
seats: {self.seats}
"""

  def start(_self):
    print("vroom vrooooom!")


print(dir(Car))
print()


class Convertible(Car):
  def __init__(self, **kwargs):
    super().__init__()
    self.roof_convert_time_s = kwargs.get("roof_convert_time_s", 5)

  def __str__(self):
    old_str = super().__str__().split('\n')
    old_str[0] = "=== Convertible ==="
    old_str[-1] = f"roof_convert_time_s: {self.roof_convert_time_s}"
    old_str.append("")
    new = "\n".join(old_str)

    return new

  def raise_roof(self):
    sleep(self.roof_convert_time_s)
    print("zuuup zuuuuup ppp")


print(dir(Convertible))
print()


porsche = Convertible(color="blue", brand="Porsche",
                      model="Boxter", roof_convert_time_s=8)
print(porsche)
porsche.start()
porsche.raise_roof()
