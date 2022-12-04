sheep_attendance = [True,  True,  True,  False,
                    True,  True,  True,  True,
                    True,  False, True,  False,
                    True, None, 1, True,
                    True,  True,  True,  True,
                    False, False, True,  True]


def count_sheep(sheep):
    x = 0
    for i in sheep:
        if i == True:
            x = x + 1
    return x


def count_sheep_2(sheep):
    return sheep.count(True)


print(count_sheep(sheep_attendance))
print(count_sheep_2(sheep_attendance))
