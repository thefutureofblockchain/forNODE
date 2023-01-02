import random
import sys

def main():
    i = 0
    lvl = get_level()

    for _ in range(10):
       try:
            d = generate_integer(lvl)
            q = generate_integer(lvl)
            c = input(f"what would {d} + {q} be")
            '''if c.isnumeric == True:
                c = int(c)
            else:
                raise ValueError'''
            ab = d + q

            for _ in range (2):
                try:
                    #if c.isnumeric == False:
                        #raise ValueError
                    if c == ab:
                        i += 1
                        break
                    elif c.isnumeric == False:
                        raise ValueError
                    else:
                        print("EEE")
                        c = int(input(f"what would {d} + {q} be"))
                except ValueError:
                    print("EEE")
                    continue
            if c != ab:
                print(d, "+", q ,"would be" ,ab)
            else:
                pass
       except ValueError:
            pass
    print("your score is", i)
    sys.exit("")



def get_level():
    while True:
        try:
            a = int(input("Enter: "))
            if a > 3 or a < 0:
                raise ValueError
            else:
                return a
                break
        except ValueError:
            continue


def generate_integer(level):
    try:
        if level == 1:
            x = 9
        elif level == 2:
            x = 99
        elif level == 3:
            x = 999
        else:
            raise ValueError
    except ValueError:
        pass
    i = random.randint(0, x )
    return i



if __name__ == "__main__":
    main()
