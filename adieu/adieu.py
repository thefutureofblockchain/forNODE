import inflect
p = inflect.engine()
ab = []
while True:
    try:
        a = input("")
        ab.append(a)
    except EOFError:
        break
cd = p.join(ab)
print("Adieu, adieu, to", cd)

