import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        a = re.search(r"([0-9]|1[1-2])\:[0-5][0-9]",s)
        if a:
            print(a)
    except ValueError:
        pass

...


if __name__ == "__main__":
    main()
