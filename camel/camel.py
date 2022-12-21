def main():
    user_input = input("Enter it: ")

    for letter in user_input:
        if letter.isupper():
            if user_input.find(al_is(user_input)) == "1":
                predecessor ,successor = user_input.split(sep = letter)
                letter = letter.lower()
                #letter = letter.replace(letter,"_"+letter)
                # print(letter)
                user_input = user_input.lower()

                #print(letter, end = "")
                print(predecessor , "_",letter,successor, sep="", end = "")
            else:
                a, predecessor ,successor = user_input.split(sep = letter)
                letter = letter.lower()
                #letter = letter.replace(letter,"_"+letter)
                # print(letter)
                user_input = user_input.lower()

                #print(letter, end = "")
                print(a, "_" , predecessor , "_",letter,successor, sep="", end = "")
        else:
            c = 1
            #print(letter, end= "")
    print()

def al_is(inpt):
    if inpt.find("A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J" or "K" or "L" or "M" or "N" or "O" or "P" or "Q" or "S" or "T" or "U" or "V" or "W" or "X" or "Y" or "Z" ) == 1:
     return 1
    else:
     return 2

main()