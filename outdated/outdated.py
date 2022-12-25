
#while True:
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

            elif "," in a:

                    a = a.replace(",", " ")
                    day,month,year = a.split()
                    day = day.strip()
                    month = month.strip()
                    year = year.strip()
                    month = mon.index(month)
                    month = int(month)
                    if int(month) > 12 or int(day) > 31:
                            raise ValueError


            print(f"{year}-{month:02}-{day:02}")

except (ValueError,KeyError):
        print("there was an error")
        pass


