items = {

}
x = 1
while True:
    try:
        items[x] = input("enter: ")
        print(items[x])
        x = x+1
    except EOFError:
    