import inflect
p = inflect.engine()
ab = []
i = 0
#mylist = p.join(("apple" , "banana"))
while True:
    try:
        a = input("Enter: ")
        ab.append(a)
        i+=1
    except EOFError:
        print()
        break
c = len(ab)
cd = p.join(ab)
#for i in range(c):
print("Adieu, Adieu to ", cd)

