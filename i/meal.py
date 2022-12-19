def main():



def convert(time):
hours, minutes = time.split(":")
mes = minutes/60
float(mes)
float(hours)
return hours + mes

if __name__ == "__main__":
    main()