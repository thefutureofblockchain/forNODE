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
        prac = []
        a = re.search(r"^((?:[0-9]|1[0-2])\:[0-5][0-9] (?:AM|PM) to (?:[0-9]|1[0-2])\:[0-5][0-9] (?:AM|PM)$)",s)
        b = re.search(r"^((?:[0-9]|1[0-2]) (?:AM|PM) to (?:[0-9]|1[0-2]) (?:AM|PM)$)",s)
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
                        num = num.strip()
                        if num == "12" or num == 12:

                            Cnum = "12"
                        else:
                            Cnum = int(num)+12
                        co.append(Cnum)
                    else:
                        Bamen = amen.replace(" AM", "")
                        Bamen = Bamen.strip()
                        if num == "12" or num == 12:
                            prenum.append(12)
                            Bnum = "00"
                            bestie.append(Bnum)
                        else:
                            Bnum = int(num)
                            prenum.append(Bnum)
                            if 10-Bnum >= 1:
                                Bnum = "0"+str(Bnum)
                            if Bnum == 12:
                                bestie.append("00")
                            else:
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
                        return f"{co[0]}:{camen[0]} to {bestie[0]}:{Bamen}"
                elif len(co) == 2:
                    return f"{co[0]}:{camen[0]} to {co[1]}:{camen[1]}"





        elif b:
                ab = str(b.groups(1))
                ab = str(ab)
                ab = ab.replace("('","")
                ab = ab.replace("',)","")
                ba = re.split("to",ab)
                for time in ba:
                    q = re.search(r"([0-9]|1[0-2]) PM", time)
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
                        ac = ac.strip()
                        prac.append(ac)
                        if 10-int(ac) >= 1:
                            ac = "0"+ac
                        t.append(ac.rstrip())
                if len(d) == 0:
                            alt = ba[0].rstrip().replace(" AM",":00")
                            emo =ba[1].rstrip().replace(" AM",":00")
                            return f"{alt} to{emo}"
                if len(d) == 1:

                        qa = d[0]
                        qa = int(qa)
                        if qa == 12:
                            qa = 12
                        else:
                            qa = qa+12
                        if t[0] == "12" or t[0] == 12:
                            cd = "00"
                        else:
                            cd = t[0]
                        qaa = t[0].replace("0","")
                        q = re.search(re.escape(qaa)+r" AM",ba[0])
                        if ba[0].startswith(qaa) and q:
                                return f"{cd}:00 to {qa}:00"
                        elif ba[0].startswith(prac[0]) == True and q:
                                return f"{cd}:00 to {qa}:00"
                        else:
                            return f"{qa}:00 to {cd}:00"
                elif len(d) == 2:
                        qa = d[0]
                        qa = int(qa)
                        if qb == 12:
                            qb = "00"
                        else:
                            qa = qa+12
                        qb = d[1]
                        qb = int(qb)
                        if qb == 12:
                            qb = "00"
                        else:
                            qb = qb+12

                        return f"{qa}:00 to {qb}:00"
        else:
            raise ValueError
    except ValueError:
        sys.exit("ValueError")



if __name__ == "__main__":
    main()
