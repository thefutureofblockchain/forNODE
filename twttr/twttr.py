def main():
    a = input("Enter eet: ")

    for letter in a:
        if letter.isupper():
            letter = letter.lower()
            x,y,z = a.partition(letter)
            print(x ,"_" , y , z, sep="", end = "")

            '''print(letter, end = "")'''
        else:
           s = 3
           # print(letter, end= "")
    print()

main()