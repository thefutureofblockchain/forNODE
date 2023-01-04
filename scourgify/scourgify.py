import sys
import csv
#try:
students = []
q = []
try:
    with open(sys.argv[1]) as file:
            if len(sys.argv) != 2 or sys.argv[2].endswith(".csv") == False:
                raise ValueError
            reader = csv.reader(file)
            for row in reader:
                if "name" in row:
                    pass
                else:
                    students.append({"name": row[0], "house": row[1]})
    for student in students:
        a = student['name']
        b = student['house']
        n1,n2 = a.split(",")
        ab = [n2,n1,b]
        q.append(ab)
    with open(sys.argv[2], "a") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for line in q:
                writer.writerow({"first": line[0],"last": line[1], "house": line[2]})
except (FileNotFoundError,ValueError,IndexError):
    sys.exit("uh oh")

