import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        a = re.search(r"((?:^[0-9]|1[1-2])\:[0-5][0-9] (?:AM|PM) to (?:[0-9]|1[1-2])\:[0-5][0-9] (?:AM|PM)$)",s)
        b = re.search(r"((?:^[0-9]|1[1-2]) (?:AM|PM) to (?:[0-9]|1[1-2]) (?:AM|PM)$)",s)
        if a:
            q = re.search()
            ab = a.groups(1).replace(q.groups(1),)
            return a
        elif b:
            ab = str(b.groups(1))
            q = re.search(r"([0-9]|1[1-2]) PM", ab)
            if q:
                
                '''qa = str(q.groups(1))
                qa = qa.replace("('","")
                qa = qa.replace("',)","")
                print(qa)
                qa = int(qa)
                qa = qa+12
                print(qa)'''
            #ab = b.groups(1).replace(q.groups(1),)
        else:
            raise ValueError
    except ValueError:
        sys.exit("did not work bro")

...


if __name__ == "__main__":
    main()
