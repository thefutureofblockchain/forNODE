def main():
    time = input("Enter: ")
    a = convert(time)
    if a >= 7 and a <= 8:
        print("breakfast time")
    elif a >= 12 and a <= 13:
        print("lunch time")
    elif a >= 18 and a <= 19:
        print("dinner time")
    else:
        x = 4


def convert(time):
    hours, minutes = time.split(":")
    mes = float(minutes)/60
    return float(hours) + mes

if __name__ == "__main__":
    main()