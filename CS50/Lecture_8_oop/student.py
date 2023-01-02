class Student:
    # i belive this variabe is called a class attribute
    # this attribute is availble to every object that is initialized by this class
    # this can be called by print(Student.test2)
    test2 = "blah"

    # the init method allows you to customize some attributes when you call them.
    # the self.name is set when you initialize the object. It can be different for each object.
    # It can return Harry in one object and Ron in another.
    def __init__(self, name, house, patronas):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house
        self.patronas = patronas

    def __str__(self):
        return f"{self.name} from house {self.house}"

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]:
            raise ValueError("Inalid House")
        else:
            self._house = house

    def charm(self):
        match self.patronas:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦫"
            case "Jack Russel terrier":
                return "🐶"
            case _:
                return "🪄"


def main():
    testobject = get_student()
    # print(f"{testobject.name} from house {testobject.house}")
    print(testobject)
    print(testobject.charm())
    print(Student.test2)


def get_student():
    name = input("name: ")
    house = input("house: ")
    patronas = input("patronas: ")
    return Student(name, house, patronas)


if __name__ == "__main__":
    main()
