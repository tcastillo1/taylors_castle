import csv

students = []

with open("students.csv") as file:
    read_my_csv = csv.reader(file)
    for row in read_my_csv:
        students.append({"name": row[0], "house": row[1]})

for student in sorted(students, key=lambda student: student["name"]):
    print(student["name"], student["house"])
