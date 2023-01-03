import tabulate
import sys
import csv

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(csvfile)
        print(tabulate(table, headers, tablefmt="plain"))

except FileNotFoundError:
    pass