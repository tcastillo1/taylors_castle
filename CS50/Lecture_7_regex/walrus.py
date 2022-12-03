import re

# walrus operator
# this operator checks if the boolean expression is true. If it is, then the code below it is ran
if walrus := (2 + 2 == 4):
    print("hello")

# you can also write the code in such a way that any value returned evaluates as True
name = "Taylor"

# dolphin is a variable that we are both creating and testing. If dolphin gets assigned to anything then it
# automatically gets evaluated as True. Joe and Bob are not in Taylor so they do not get evaluated as True,
# but "aylo" is in Taylor, so it gets evaluated as True and moves on to the print statement
if dolphin := re.search("(Joe|Bob|aylo)", name):
    print("hello Taylor")
