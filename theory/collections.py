# python3 theory/collections.py

print("=== Lists ===")
print("ordered, changeable and indexed")
days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(type(days))
print(days)
print('Mon' in days)
print(days[0])
print(days[3])
print(len(days))
days.append("Sat")
print(days)
print(len(days))


print()
print("=== Tuples ===")
print("ordered, unchangeable and indexed")
days = ("Mon", "Tue", "Wed", "Thur", "Fri")
print(type(days))
print(days)
print('Mon' in days)
print(days[0])
print(days[3])
print(len(days))


print()
print("=== Sets ===")
print("unordered, unchangeable and unindexed")
days = {"Mon", "Tue", "Wed", "Thur", "Fri"}
print(type(days))
print(days)
print('Mon' in days)
print(len(days))


print()
print("=== Dictionarys ===")
print("key-value pairs")
luis = {
    "name": "luis",
    "age": 19,
    "korean": False,
    "fav_foods": ["pizza", "staek"]
}
print(type(luis))
print(luis)
print('name' in luis)
print(luis["name"])
print(luis["fav_foods"])
print(19 in luis)
print(len(luis))
