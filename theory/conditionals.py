# python3 theory/conditionals.py

def plus(a, b):
    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return a + b
        else:
            return None
    else:
        return None


print(plus(1, '10'))


def can_drink(age):
    print(f"You are {age} years old.")

    if age < 18:
        print("You can't drink.")
    elif age == 18 or age == 19:
        print("Go easy on it cowbow.")
    elif age > 19 and age < 25:
        print("Buckle up son.")
    else:
        print("Enjoy your drink!")


can_drink(17)
can_drink(19)
can_drink(21)
can_drink(25)
