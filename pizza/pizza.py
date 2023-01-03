import tabulate
import sys
import csv

try:
    with open(sys.argv[1], "r") as file:
        if len(sys.argv) != 2:
            raise FileNotFoundError
        
        reader = csv.reader(file)
        '''read = csv.reader(file)'''
        table = reader
        print(tabulate.tabulate(table, tablefmt="grid"))

except (FileNotFoundError,IndexError):
    sys.exit("there was an error")