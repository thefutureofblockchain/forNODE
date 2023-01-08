import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        d = []
        t = []
        co = []
        bestie = []
        camen = []
        prenum = []
        a = re.search(r"((?:^[0-9]|1[1-2])\:[0-5][0-9] (?:AM|PM) to (?:[0-9]|1[1-2])\:[0-5][0-9] (?:AM|PM)$)",s)
        b = re.search(r"((?:^[0-9]|1[1-2]) (?:AM|PM) to (?:[0-9]|1[1-2]) (?:AM|PM)$)",s)
        if a:
                ab = str(a.groups(1))
                ab = str(ab)
                ab = ab.replace("('","")
                ab = ab.replace("',)","")
                ba = re.split("to",ab)
                for time in ba:
                    time = re.split(r"\:",time)
                    num = time[0]
                    amen = time[1]
                    de = re.search(r"PM",amen)
                    if de:
                        Camen = amen.replace(" PM", "")
                        Camen = Camen.strip()
                        camen.append(Camen)
                        Cnum = int(num)+12
                        co.append(Cnum)
                    else:
                        Bamen = amen.replace(" AM", "")
                        Bamen = Bamen.strip()
                        Bnum = int(num)
                        prenum.append(Bnum)
                        if 10-Bnum > 1:
                            Bnum = "0"+str(Bnum)
                        bestie.append(Bnum)

                if len(co) == 0:
                        lm = ba[0].replace(" AM","")
                        ln = ba[1].replace(" AM","")
                        return f"{lm}to{ln}"
                elif len(co) == 1:
                    l = str(prenum[0])
                    l = l+f":{Bamen} AM"
                    if l in ba[0]:
                        return f"{bestie[0]}:{Bamen} to {co[0]}:{camen[0]}"

                    else:
                        return f"{co[0]}:{Camen[0]} to {bestie[0]}:{Bamen}"
                elif len(co) == 2:
                    return f"{co[0]}:{camen[0]} to {co[1]}:{camen[1]}"





        elif b:
                ab = str(b.groups(1))
                ab = str(ab)
                ab = ab.replace("('","")
                ab = ab.replace("',)","")
                ba = re.split("to",ab)
                for time in ba:
                    q = re.search(r"([0-9]|1[1-2]) PM", time)
                    if q:
                        ac = q.groups(1)
                        ac = str(ac)
                        ac = ac.replace("('","")
                        ac = ac.replace("',)","")
                        d.append(ac)
                    else:
                        if time == ba[0]:
                            nonea = 1
                        ac = time.replace("AM","")
                        t.append(ac.rstrip())
                if len(d) == 0:
                            alt = ba[0].rstrip().replace(" AM",":00")
                            emo =ba[1].rstrip().replace(" AM",":00")
                            return f"{alt} to{emo}"
                if len(d) == 1:

                        qa = d[0]
                        qa = int(qa)
                        qa = qa+12

                        if t[0] in ba[0]:
                            return f"{t[0]}:00 to {qa}:00"
                        else:
                            return f"{qa}:00 to{t[0]}:00"
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
