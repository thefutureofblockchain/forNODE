items = {

}
x = 1
while True:
    try:
        item = input("").upper()
        if item in items:
            items[item] = items[item] + 1
        else:
            items[item] = 1
    except EOFError:
        for k, v in sorted(items.items()):
           print(v,k)
        break




