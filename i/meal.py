def main():
    time = input("Enter: ")
    convert(time)
    if time > 7 and time < 8:
        print("breakfast time")
    elif time > 12 and time < 13:
        print("lunch time")
    elif time > 18 and time < 19:
        print("dinner time")
    else:
        x = 4


def convert(time):
    hours, minutes = time.split(":")
    mes = minutes/60
    float(mes)
    float(hours)
    return hours + mes

if __name__ == "__main__":
    main()