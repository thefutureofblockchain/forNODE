def main():
    user_input = input("Enter it: ")

    for letter in user_input:
        if letter.isupper():
            predecessor ,successor = user_input.split(sep = letter)
            letter = letter.lower()
            #letter = letter.replace(letter,"_"+letter)
            # print(letter)
            user_input = user_input.lower()

            #print(letter, end = "")
            print(predecessor , "_",letter,successor, sep="", end = "")
        else:
            c = 1
            #print(letter, end= "")
    print()

main()