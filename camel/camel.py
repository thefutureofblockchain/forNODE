def main():
    a = input("Enter it: ")

    for letter in a:
        if letter.isupper():
            letter = letter.lower()
            x,y,z = a.partition(letter)
            print("_" ,y,z, sep="", end = "")

            '''print(letter, end = "")'''
        else:
           print(letter, end= "")
    print()

main()