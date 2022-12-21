def main():
    a = input("Enter eet: ")

    for letter in a:
        if letter.isupper():
            x,y,z = a.partition(letter)
            print(y)
            letter = letter.lower()
            print(letter, end = "")
        else:
            print(letter, end= "")
    print()

main()