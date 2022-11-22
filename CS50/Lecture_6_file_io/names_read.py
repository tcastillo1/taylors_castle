with open("names.txt", "r") as file:
    for line in file:
        print("Hello, ", line.rstrip())

# this also works:
# file = open("names.txt", "r")

# for line in file:
#     print("Hello, ", line.rstrip())
