def main():
    xy = input("Enter: ")
    print(gauge(per(convert(xy))))


def convert(f):
    while True:
        try:
            x,y = f.split(sep = "/")
            x = int(x)
            y = int(y)
            if x>y and y>0:
                continue
            perc =x/y*100
            return perc
        except ValueError:
            print("x and y are not integers")
            pass
        except ZeroDivisionError:
            print("You divided by zero")
            pass
def gauge(percentage):
    if percentage > 1 and percentage < 99:
        percentage = str(percentage)
        a = percentage + "%"
        return a
    elif percentage == 1 or percentage == 0:
        return("E")
    elif percentage == 99 or percentage == 100:
        return("F")
def per(c):
    c = round(c)
    return c
if __name__ == "__main__":
    main()