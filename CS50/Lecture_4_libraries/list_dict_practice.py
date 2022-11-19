list_with_dict = [{"Harry": "Gryf", "Draco": "Slyth"}]

# because this list only has 1 item in it, printing index 0 prints the entire dictionary
print(list_with_dict[0])

# x stores the dictionary
x = list_with_dict[0]

# now that we have a dictionary, we can find the key value pair for draco
print(x["Draco"])


# it is not as clean but this also works. What is it doing? It is finding the first element in the list_with_dict which is a list.
# the first element of the list "list_with_dict" is pulled using an index of 0. this returns a dictionary
# now that we have a dictionary, we can call ["Harry"] and return it's key value pair of "Gryf"
print(list_with_dict[0]["Harry"])
