def main():
    xy = get_frac()
    percentage = per(xy)
    if percentage > 1 and percentage < 99:
        print(percentage,"%",sep="")
    elif percentage == 1 or percentage == 0:
        print("E")
    elif percentage == 99 or percentage == 100:
        print("F")

def get_frac():
    while True:
        try:
            xy = input("What's x/y?")
            x,y = xy.split(sep = "/")
            x = int(x)
            y = int(y)
            if x>y and y>0:
                print("X is bigger than y")
            perc =x/y*100
            return perc
        except ValueError:
            print("x and y are not integers")
            pass
        except ZeroDivisionError:
            print("You divided by zero")
            pass

def per(c):
    c = round(c)
    return c
main()



