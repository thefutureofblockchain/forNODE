def main():
    mon = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    a = input("enterr")
    c = conv(a)
def conv(n):
    try:
            mon = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
            ]

            if "/" in n:
                    month, day, year = n.split(sep = "/")
                    month = int(month)
                    day = int(day)
                    year = int(year)
                    '''month = 'month:02'
                    day = 'day:02'''
                    print(year,"-",month, "-",day)

            elif "," in n:
                    n = n.replace(",", " ")
                    month, day, year = n.split()
                    month = mon.index(month)
                    month = int(month)
                    if is_char(month) == True:
                        month = ("0" + month)
                    if is_char(day) == True:
                         day = ("0" + day)
                    print(year,"-",month, "-",day,sep="")
            if month > 12 or day > 31:
                    raise ValueError

    except (ValueError,KeyError):
        pass
def is_char(i):
    if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i ==7 or i == 8 or i == 9:
        return True
    else:
        return False

main()
