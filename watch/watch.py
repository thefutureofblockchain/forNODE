import re
import sys
def main():
    print(parse(input("HTML: ")))
def parse(s):

    string = re.search(r'(src="http(?:s)?://(?:www.)youtube.com/embed/[\w]+)',s)
    if string:
        print(string)
    else:
        print(string)
        print("SEE BITCH")
if __name__ == "__main__":
    main()
