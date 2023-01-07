import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        a = re.search(r"((?:^[0-9]|1[1-2])\:[0-5][0-9] (?:AM|PM) to (?:[0-9]|1[1-2])\:[0-5][0-9] (?:AM|PM)$)",s)
        b = re.search(r"((?:^[0-9]|1[1-2]) (?:AM|PM) to (?:[0-9]|1[1-2]) (?:AM|PM)$)",s)
        if a or b:
            print(a,b)
        else:
            print("hello")
    except ValueError:
        pass

...


if __name__ == "__main__":
    main()
