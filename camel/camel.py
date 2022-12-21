def main():
    a = input("Enter it: ")

    for letter in a:
        if letter.isupper():
            letter = letter.lower()
            a = a.lower()
            x,y,z = a.partition(letter)
            #print(letter, end = "")
            print("_" ,x, sep="", end = "")
        else:
            s = 3
            #print(letter, end= "")
    print()

main()