def main():
    a = input("Enter eet: ")

    for letter in a:
        '''lets, me = a.split(isupperr(letter))
        print(lets , me )'''
        if letter.isupper():
            lets, me = a.split(letter.isupper)
            letter = letter.lower()
            print(letter, end = "")
        else:
            print(letter, end= "")
    print()

