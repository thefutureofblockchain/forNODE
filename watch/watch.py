import re
import sys
def main():
    print(parse(input("HTML: ")))
def parse(s):

    string = re.search(r'src="(http(?:s)?://(?:www.)youtube.com/embed/[\w]+)',s)
    if string:
        a = str(string.groups(1))
        a = a.replace("youtube","youtu.be")
        if "www." in a:
            a = a.replace("www.","")
        a = a.replace("/embed","")
        a = a.replace("('","")
        a = a.replace("',)","")
        return a
    else:
        return None
if __name__ == "__main__":
    main()
