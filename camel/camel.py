def main():
    user_input = input("Enter it: ")

    for letter in user_input:
        if letter.isupper():
            letter = letter.lower()
            user_input = user_input.lower()
            x,y,z = user_input.partition(letter)
            #print(letter, end = "")
            print("_" ,y,z, sep="", end = "")
        else:
            a = 1 
            # print(letter, end= "")
    print()

main()