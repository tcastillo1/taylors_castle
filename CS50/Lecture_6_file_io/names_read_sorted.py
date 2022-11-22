list_unsorted = []

with open("names.txt", "r") as file:
    for line in file:
        list_unsorted.append("Hello, " + line.rstrip())

for i in sorted(list_unsorted):
    print(i)
