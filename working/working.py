import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        a = re.search(r"[\d]")
    except ValueError:


...


if __name__ == "__main__":
    main()
