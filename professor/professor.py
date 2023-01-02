import random


def main():
    lvl = get_level()

    for _ in range(10):
        d = generate_integer(lvl)
        q = generate_integer(lvl)
        c = int(input(f"what would {d} + {q} be"))
        ab = d + q

        for _ in range (2):
                if c == ab:
                    break
                else:
                    print("EEE")
                    c = int(input(f"what would {d} + {q} be"))
        if c != ab:
            print(d, "+", q ,"would be" ,ab)
        else:
            pass


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
