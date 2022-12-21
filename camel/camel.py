def main():
    user_input = input("Enter it: ")

    for letter in user_input:
        if letter.isupper():
            predecessor ,partition ,successor = user_input.partition(letter)
            letter = letter.lower()
            letter = letter.replace(letter,"_"+letter)
            # print(letter)
            user_input = user_input.lower()

            #print(letter, end = "")
            print(predecessor , letter,successor, sep="", end = "")
        else:
            c = 1 
            #print(letter, end= "")
    print()

main()