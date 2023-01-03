import sys
a = []
try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            if line.startswith("#") == True or line.isspace() == True or line.startswith("'''") == True:
                pass
            else:
                a.append(line)
            if len(sys.argv) != 2:
                raise ValueError
            if sys.argv[1].endswith(".py") == False:
                raise ValueError
    print(len(a))
except (ValueError , IndexError):
    sys.exit("Too many or too few args")
except FileNotFoundError:
    sys.exit("File wasn't found")