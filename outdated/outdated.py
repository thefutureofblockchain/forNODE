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
                    '''month = month:02'''
                    day = 'day:02'
                    print(year,"-",month, "-",day,sep="")
            if month > 12 or day > 31:
                    raise ValueError

    except (ValueError,KeyError):
        pass

main()
