# this function creates a staircase starting at the top level and then looping until it reaches the ground floor
def mario_climb(x):
    i = 1
    x = int(input("How many stairs will mario climb? "))
    while i < x + 1:
        print((x - i) * " ", "#" * i, sep="")
        i = i + 1


mario_climb(5)
