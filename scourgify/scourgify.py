import sys
import csv
#try:
students = []
q = []
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
    a = student['name']
    b = student['house']
    n1,n2 = a.split(",")
    ab = [n2,n1,b]
    q.append(ab)
print(q)
with open(sys.argv[2], "a") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for line in q:
            print(line)


            writer.writerow({"first": line[0],"last": line[1], "house": line[2]})


