import re
import sys
def main():
    print(parse(input("HTML: ")))
def parse(s):
    s = s.split("src")
    print(s)
    string = re.sub("","",s)
if __name__ == "__main__":
    main()
