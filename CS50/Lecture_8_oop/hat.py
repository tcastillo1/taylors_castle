from random import randint

# we dont use the init method here because we don't need custom versions of the sorting hat.
# there is only one sorting hat so we leave it as "Hat" and we omit the __init__ method


class Hat:
    house = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    x = randint(0, 3)

    @classmethod
    def sort(cls, name):
        rand_house = cls.house[cls.x]
        return f"{name} is in house {rand_house}"


print(Hat.sort("Tay"))
# print(type(Hat))
# print(type(Hat.sort))
# print(type(Hat.sort("Harry")))
