from datetime import date
import inflect

def main():
    dateInputted = input("year: ")
    dateInputted = dateInputted.split("-")
    print(date())
    print(date.today())


...


if __name__ == "__main__":
    main()
