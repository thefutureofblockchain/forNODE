from datetime import date
import inflect
import sys

def main():
    try:
        dateInputted = input("year: ")
        year, month, _date = dateInputted.split("-")
        year = int(year)
        month = int(month)
        _date = int(_date)
        print(date(year,month,_date))
        print(date.today())
    except ValueError:
        sys.exit("Something went wrong")


...


if __name__ == "__main__":
    main()
