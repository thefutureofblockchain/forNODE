def main():
    user_input = input("Enter it: ")

    for letter in user_input:
        if letter.isupper():
            letter = letter.replace(letter,"_"+letter)
            print(letter)
            '''user_input = user_input.lower()
            predecessor ,partition ,successor = user_input.partition(letter)
            #print(letter, end = "")
            print("_" ,partition,successor, sep="", end = "")
        else:
            a = 1
            # print(letter, end= "")'''
    print()

main()