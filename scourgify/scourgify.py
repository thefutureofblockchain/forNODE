import sys
try:
    with open(sys.argv[1]) as file:
        for line in file:
            name, house = line.rstrip().split(",")
            print(f"{name} is in {house}")
except (FileNotFoundError, ValueError, IndexError):
    sys.exit("uh oh")
