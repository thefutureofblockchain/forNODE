import random


def main():
    lvl = get_level()

def get_level():
    while True:
        try:
            a = int(input("Enter: "))
            if a > 3 and a < 0:
                raise ValueError
            else:
                break
        except ValueError:
            continue


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
