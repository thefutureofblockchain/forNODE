a = input("Enter: ")
for letter in a:
    if letter.isupper():
        a = a.replace(letter, "_" + letter.lower())
print(a)
