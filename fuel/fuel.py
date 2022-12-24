def main():
    xy = get_frac()
    percentage = per(xy)
    print(percentage)
def get_frac():
    while True:
        try:
            xy = input("What's x/y?")
            x,y = xy.split(sep = "/")
            print(x,y)
            int(x)
            int(y)
            if x<=y:
                perc =int(x/y*100)
                return perc
            else:
                pass
        except ValueError:
            print("x and y are not integers")
            pass
        except ZeroDivisionError:
            print("You divided by zero")
            pass
def per(c):
    c = round(c)
    if c > 1 and c < 99:
        return c
    elif c <= 1:
        return "E"
    elif c <= 99:
        return"F"
main()



