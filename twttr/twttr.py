a = input("Enter EETODK: ")
for letter in a:
    letter = letter.lower()
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        continue
    print(letter)