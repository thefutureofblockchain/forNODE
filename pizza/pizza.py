import tabulate
import sys
import csv

try:
    with open(sys.argv[1], "r") as file:
        if len(sys.argv) != 2:
            raise FileNotFoundError
        if sys.argv[1].endswith(".csv") == False:
            raise FileNotFoundError
        reader = csv.DictReader(file)
        '''read = csv.reader(file)'''
        table = reader
        header = csv.reader(file)
        print(header)
        print(tabulate.tabulate(table, header,tablefmt="grid"))

except (FileNotFoundError,IndexError):
    sys.exit("there was an error")