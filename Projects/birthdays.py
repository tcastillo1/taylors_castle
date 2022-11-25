import datetime as dt
import csv

x = dt.datetime.now().strftime("%x")
y = dt.datetime(1990, 8, 21).year
z = dt.date.today()

file = open("birthdays.csv", "r")
print(file)

birthdays = []

birthdays.append({"name": "Jordan", "birthday": y})

print(x)
print(y)
print(z)
print(birthdays)
