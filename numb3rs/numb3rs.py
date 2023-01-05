import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    num = re.search(r"^([0-255]\.[0-255]\.[0-255]\.[0-255])$", ip)
    if num:
        return num.group(1)
    else:
        return num.group(1)





if __name__ == "__main__":
    main()

