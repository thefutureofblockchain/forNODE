def main():
    a = input("Enter eet: ")

    for letter in a:
        if letter.isupper():
            letter = letter.lower()
            x,y,z = a.partition(letter)
            print(x , end = "")

            '''print(letter, end = "")'''
        '''else:
            print(letter, end= "")'''
    print()

main()