def main():
    a = input("Enter eet: ")

    for letter in a:
        lets, me = a.split(letter.isupper)
        print(lets , me )
        '''if letter.isupper():
            lets, me = a.split(letter.isupper)
            letter = letter.lower()
            print(letter, end = "")
        else:
            print(letter, end= "")
    print()'''
def isupperr(letter):
    if letter.isupper():
        return letter
    else:
        

