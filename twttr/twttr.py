a = input("Enter eet: ")
for letter in a:
    if letter.isupper():
        letter = letter.lower()
        print(letter)
    else:
        print(letter)
