items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
a = 0
while True:
    try:
        ite = input("Item: ")
        ite = ite.title()
        a = a+items[ite]
        a = float(a)
        print("$",a, sep="")
    except ValueError:
        pass
    except KeyError:
        print("There was an error")
        pass
    except EOFError:
        print()
        break

