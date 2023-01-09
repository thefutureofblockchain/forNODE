from datetime import date
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
        get_difference(date(year,month,_date))
    except ValueError:
        sys.exit("Something went wrong")


def get_difference(y):
    try:
        diff = date.today() - y
        print(diff)
    except ValueError:
        sys.exit("wtf bro")



if __name__ == "__main__":
    main()
