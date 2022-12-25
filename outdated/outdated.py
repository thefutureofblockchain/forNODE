
while True:
        try:
                a = input("enter: ")
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
                if "/" in a:
                        month, day, year = a.split(sep = "/")
                        month = int(month)
                        day = int(day)
                        year = int(year)
                        if int(month) > 12 or int(day) > 31:
                                raise ValueError
                        break
                elif "," in a:
                        a = a.replace(",", " ")
                        print(a)
                        month,day,year = a.split()
                        day = day.strip()
                        day = int(day)
                        month = month.strip()
                        month = month.title()
                        year = year.strip()
                        month = mon.index(month)
                        month = int(month)
                        month += 1
                        if not month in mon:
                                raise KeyError
                        if int(month) > 12 or int(day) > 31:
                                raise ValueError
                        break
        except (ValueError,KeyError):
                continue
print(f"{year}-{month:02}-{day:02}")

