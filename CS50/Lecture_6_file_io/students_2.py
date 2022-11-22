students = []

with open("students.csv", "r") as file:
    for i in file:
        name, house = i.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for i in sorted(students, key=lambda student: student["name"]):
    print(i["name"], i["house"])

print(student["name"])
print(students)
