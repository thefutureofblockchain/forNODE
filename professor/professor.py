import random


def main():
    lvl = get_level()
    d = generate_integer(lvl)
    q = generate_integer(lvl)
    for _ in range(10):
        print("what would" ,d ,"+" ,q ,"be")

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
