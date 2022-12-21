def main():
    a = input("Enter it: ")

    for letter in a:
        if letter.isupper():
            b = letter.lower()
            x,y,z = a.partition(b)
            #print(letter, end = "")
            print("_" ,y,z, sep="", end = "")
        else:
            s = 3
            #print(letter, end= "")
    print()

main()