import re
import sys
def main():
    print(parse(input("HTML: ")))
def parse(s):

    string = re.search(r'src="(https?://(?:www)?.youtube.com/embed/+)" ',s)
    if string:
        print(string)
    else:
        print("SEE BITCH")
if __name__ == "__main__":
    main()
