import sys
import csv
#try:
students = []
with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            if "name" in row:
                pass
            else:
                students.append({"name": row[0], "house": row[1]})
                '''b = students.index(row[0])
                a = students[b]
                a = a.rstrip().split(",")
                print(a)'''
for student in students:
#b = students.index()
    a = students[0]
    #a = a.rstrip().split(",")
    print(a)
    #print(f"{student['name']} is from {student['house']}")
