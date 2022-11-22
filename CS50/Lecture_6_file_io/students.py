students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # student = {"name": name, "house": house}
        student = {name: house}
        students.append(student)

print(students)
