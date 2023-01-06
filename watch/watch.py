import re
import sys
def main():
    print(parse(input("HTML: ")))
def parse(s):

    string = re.search(r'src="(http(?:s)?://(?:www.)youtube.com/embed/[\w]+)',s)
    if string:
        a = str(string.groups(1))
        a = a.replace("youtube","youtu.be")
        a = a.replace("/embed","")
        return a
    else:
        return None
if __name__ == "__main__":
    main()
