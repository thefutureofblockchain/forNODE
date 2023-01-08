import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    b = 0
    s = s.split(" ")
    for word in s:

        q = re.search(r"(\bum\b)|(^um$)",word, re.IGNORECASE)
        if q:
            b+=1
    return b


...


if __name__ == "__main__":
    main()
