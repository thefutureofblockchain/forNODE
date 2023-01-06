import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit()


def validate(ip):
    num = re.fullmatch(r"(\d{1,3}\.\d{1.3}\.\d{1,3}\.\d{1.3})",ip,re.ASCII)
    if num:
        return True
    else:
        print(num)
        return False





if __name__ == "__main__":
    main()

