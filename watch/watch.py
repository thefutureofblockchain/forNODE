import re
import sys
def main():
    print(parse(input("HTML: ")))
def parse(s):

    string = re.search(r'src="(http(?:s)?://(?:www.)youtube.com/embed/[\w]+)',s)
    if string:
        a = string.groups(1).replace("youtube","you)
    else:
        print(string)
        print("SEE")
if __name__ == "__main__":
    main()
