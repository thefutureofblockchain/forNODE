import re
import sys
def main():
    print(parse(input("HTML: ")))
def parse(s):

    string = re.search(r'src="(https?\:\/\/(?:www\.)?youtube\.com\/embed\/xvFZjo5PgG0)" ',s)
    if string:
        f = re.sub()
    else:
        print("SEE BITCH")
if __name__ == "__main__":
    main()
