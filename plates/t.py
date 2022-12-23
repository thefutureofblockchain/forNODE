c = input("Enterr")
for letter in c:
    if letter.isdigit():
       qa, b, d = c.partition(letter)
       print(qa, b, d)
       if d.isdigit() or d == 0:
        print("yes")
       else:
        print("no")
