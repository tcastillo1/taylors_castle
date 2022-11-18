students = [
    {"name":"Harry", "house":"Gryffindor", "hair":"brown"},
    {"name": "Ron", "house": "Gryffindor", "hair": "orange"},
    {"name": "Draco", "house": "Gryffindor", "hair": "yellow"}
]

for i in students:
    print(i["name"] + ",", i["hair"] + " hair")

# students has a length of 3, meaning each dictionary is 1 element in the list
print(len(students))
