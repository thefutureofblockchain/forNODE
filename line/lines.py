import sys
a = []
try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            if line.startswith("#") == True or line.isspace() == True:
                pass
            else:
                a.append(line)
    print(len(a))
except ValueError:
    sys.exit("Too many or too few args")