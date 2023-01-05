import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    num = re.fullmatch(r"^[0-255]\.$", ip)
    if num:
        return num
    else:
        return "no"





if __name__ == "__main__":
    main()

