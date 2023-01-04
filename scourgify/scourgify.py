import sys
import csv
#try:
students = []
with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            students.append({"name": row[0], "house": row[1]})
            a = students[row[0]]
            a = a.rstrip().split(",")
            print(a)
