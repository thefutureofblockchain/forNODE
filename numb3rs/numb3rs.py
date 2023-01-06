import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit()


def validate(ip):
    num = re.search("^([0,2].[0,5]?.[0,5]?.)",ip)
    if num:
        return True
    else:
        return False





if __name__ == "__main__":
    main()

