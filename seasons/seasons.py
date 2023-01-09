from datetime import date, timedelta
import inflect
import sys
p = inflect.engine()
def main():
    try:
        dateInputted = input("year: ")
        year, month, _date = dateInputted.split("-")
        year = int(year)
        month = int(month)
        _date = int(_date)
        minutes = get_difference(date(year,month,_date))
        a = conv(minutes)
        print(a, "minutes")

    except ValueError:
        sys.exit("Something went wrong")


def get_difference(y):
    try:
        diff = date.today() - y
        diff = str(diff)
        diff = diff.split(",")
        days = diff[0]
        days = days.replace(" days","")
        days = int(days)
        mins = days*24*60
        return mins
    except ValueError:
        sys.exit("wtf bro")
def conv(s):
    to_ret = p.number_to_words(s)
    to_ret = to_ret.replace("and ","")
    to_ret = to_ret.capitalize()
    return to_ret




if __name__ == "__main__":
    main()
