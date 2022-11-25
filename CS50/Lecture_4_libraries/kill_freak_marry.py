import random as rd


def kfm(a, b, c):
    names = [a, b, c]
    for j in range(3):
        action = ["kill", "freak", "marry"]
        x = rd.choice(names)
        location = names.index(x)
        print(action[j], x)
        del names[location]


kfm("melania", "megan fox", "mila kunis")
