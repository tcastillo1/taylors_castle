import csv

name = input("What is your name? ")
house = input("What house are you in? ")

file = open("csv_write.csv", "a")
file2 = csv.DictWriter(file, fieldnames=["name", "house"])
file2.writerow({"name": name, "house": house})
