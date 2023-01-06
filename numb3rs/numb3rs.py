import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit()


def validate(ip):
    num = re.fullmatch('''([01]?(?:[0-9][0-9])?|(?:25[0-5])\.
    [01]?(?:[0-9][0-9])?|(?:25[0-5])\.
    [01]?(?:[0-9][0-9])?|(?:25[0-5])\.
    [01]?(?:[0-9][0-9])?|(?:25[0-5]))''',ip)
    if num:
        return True
    else:
        print(num)
        return False





if __name__ == "__main__":
    main()

