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
        FinalReturn = convert_it(minutes)
    except ValueError:
        sys.exit("Something went wrong")


def get_difference(y):
    try:
        diff = date.today() - y
        print(date.today(),y )
        diff = str(diff)
        diff = diff.split(",")
        print(diff[0])
        days = diff[0]
        days = days.replace(" days","")
        days = int(days)
        mins = days*24*60
        print(mins)
        return mins
    except ValueError:
        sys.exit("wtf bro")
def convert_it(s):
    to_ret = p.number_to_words(s)
    to_ret = to_ret.replace("and ","")
    print(to_ret,"minutes")



if __name__ == "__main__":
    main()
