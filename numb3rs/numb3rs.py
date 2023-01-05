import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit()


def validate(ip):
    num = re.search(r"^([0-255]+\.[0-255]+\.[0-255]+[0-255]+)", ip)
    if num:
        return True
    else:
        return False





if __name__ == "__main__":
    main()

