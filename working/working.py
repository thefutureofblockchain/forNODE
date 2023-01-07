import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        d = []
        t = []
        a = re.search(r"((?:^[0-9]|1[1-2])\:[0-5][0-9] (?:AM|PM) to (?:[0-9]|1[1-2])\:[0-5][0-9] (?:AM|PM)$)",s)
        b = re.search(r"((?:^[0-9]|1[1-2]) (?:AM|PM) to (?:[0-9]|1[1-2]) (?:AM|PM)$)",s)
        if a:
            q = re.search()
            ab = a.groups(1).replace(q.groups(1),)
            return a
        elif b:
                ab = str(b.groups(1))
                ab = str(ab)
                ab = ab.replace("('","")
                ab = ab.replace("',)","")
                ba = re.split("to",ab)
                for time in ba:
                    q = re.search(r"([0-9]|1[1-2]) PM", time)
                    if q:
                        if time == ba[0]:
                            nonea = 1
                            noneb = "y"
                        ac = q.groups(1)
                        ac = str(ac)
                        ac = ac.replace("('","")
                        ac = ac.replace("',)","")
                        d.append(ac)
                    else:
                        ac = re.sub("PM","",time)
                        t.append(ac)
                        print(t)
                if len(d) == 1:
                        qa = d[0]
                        qa = int(qa)
                        qa = qa+12
                        return f"{qa}:00 to :00"
                elif len(d) == 2:
                        qa = d[0]
                        qa = int(qa)
                        qa = qa+12
                        qb = d[1]
                        qb = int(qb)
                        qb = qb+12
                        return f"{qa}:00 to {qb}:00"
        else:
            raise ValueError
    except ValueError:
        sys.exit("did not work bro")

...


if __name__ == "__main__":
    main()
