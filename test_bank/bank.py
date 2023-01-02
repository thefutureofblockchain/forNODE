def main():
    a = input("Enter: ")
    print(value(a))


def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("h") == True and greeting != "hello":
        return 20
    elif greeting.startswith("hello"):
        return 0
    else:
        return 100

if __name__ == "__main__":
    main()
