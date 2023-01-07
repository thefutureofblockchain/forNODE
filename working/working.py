import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        a = re.search(r"([0-9]|1[1-2])\:[0-5][0-9]")
        if a:
            print(a)
    except ValueError:
        

...


if __name__ == "__main__":
    main()
