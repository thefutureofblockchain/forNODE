import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit()


def validate(ip):
    num = re.fullmatch(r'''
    (1[0-9][0-9])|([0-9][0-9])|(2[0-4][0-9])
    (1[0-9][0-9])|([0-9][0-9])|(2[0-4][0-9])
    (1[0-9][0-9])|([0-9][0-9])|(2[0-4][0-9])
    (1[0-9][0-9])|([0-9][0-9])|(2[0-4][0-9])
                        ''',ip,re.ASCII)
    q = re.fullmatch(r"[0-9]|(2[0-5][0-5])",ip)
    if num or q:
        return True
    else:
        return False





if __name__ == "__main__":
    main()

