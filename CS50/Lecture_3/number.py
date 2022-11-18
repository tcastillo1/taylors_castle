# this code will copntinually prompt the user to input an integer until they actually put in an integer
while True:
    try:
        x = int(input("what is x? "))
        break
    except ValueError:
        print("x is not an integer")

print(x**3)


# rather than tell the use this isnt an int, we just "pass" on the error and loop back to asking them to input an int again
while True:
    try:
        y = int(input("what is y? "))
        break
    except ValueError:
        pass

print("y =", y)
