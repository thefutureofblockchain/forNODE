import re
import sys
def main():
    print(parse(input("HTML: ")))
def parse(s):

    string = re.search(r"<iframe width="560" height="315" src="(https://www.youtube.com/embed/xvFZjo5PgG0)" title="YouTube video player" frameborder="0" allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen\>\<\iframe\>","",s)
    if string:
        print(string)
    else:
        print("SEE BITCH")
if __name__ == "__main__":
    main()
