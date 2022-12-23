c = input("Enterr")
for letter in c:
    if letter.isdigit():
       qa, b = c.split(sep = letter)
       print(qa)
       print(b)