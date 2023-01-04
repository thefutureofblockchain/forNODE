import sys
import csv
#try:
with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for line in reader:
            name1, house = line.rstrip().split(",")
            print(f"{name1} is in {house}")
#except (FileNotFoundError, ValueError, IndexError):
    #sys.exit("uh oh")
