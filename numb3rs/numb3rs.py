import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit()


def validate(ip):
    num = re.fullmatch(r"((1[0-9][0-9])|([0-9][0-9])|(2[0-4][0-9])|[0-9]|(2[0-5][0-5]))\.",ip,re.ASCII)
    if num:
        return True
    else:
        return False





if __name__ == "__main__":
    main()

