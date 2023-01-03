import tabulate
import sys
import csv

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        table = reader

        print(tabulate.tabulate(table, tablefmt="grid"))

except FileNotFoundError:
    sys.exit("there was an error")