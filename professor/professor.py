import random
import sys

def main():
    i = 0
    lvl = get_level()

    for _ in range(10):
       try:
            d = generate_integer(lvl)
            q = generate_integer(lvl)
            c = input(f"{d} + {q} = ")
            '''if c.isnumeric == True:
                c = int(c)
            else:
                raise ValueError'''
            ab = d + q

            for _ in range (2):
                try:
                    c = int(c)
                    if c == ab:
                        i += 1
                        break
                    else:
                        print("EEE")
                        c = input(f"{d} + {q} = ")
                except ValueError:
                    print("EEE")
                    c = input(f"{d} + {q} = ")
                    continue
            if int(c) != ab:
                print(d, "+", q ,"=" ,ab)
            else:
                pass
       except ValueError:
            pass
    print("your score is", i)
    sys.exit



def get_level():
    while True:
        try:
            a = int(input("Enter: "))
            if a > 3 or a <= 0:
                raise ValueError
            else:
                return a
                break
        except ValueError:
            continue


def generate_integer(level):
    try:
        if level == 1:
            y = 0
            x = 9
        elif level == 2:
            y = 10
            x = 99
        elif level == 3:
            y = 100
            x = 999
        else:
            raise ValueError
    except ValueError:
            pass
    i = random.randint(y, x)
    return i



if __name__ == "__main__":
    main()
