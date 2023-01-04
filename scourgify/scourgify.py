import sys
import csv
#try:
students = []
with open(sys.argv[1]) as file:
        reader = csv.Dicteader(file)
        for row in reader:
            students.append({"name": row[0], "house": row[1]})
            b = students.index(row[0])
            a = students[b]
            a = a.rstrip().split(",")
            print(a)
