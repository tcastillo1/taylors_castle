class Student:
    def __init__(self, name, house, patronas):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]:
            raise ValueError("Missing or invalid house")
        self.name = name
        self.house = house
        self.patronas = patronas

    def __str__(self):
        return f"{self.name} from house {self.house}"

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


def get_student():
    name = input("name: ")
    house = input("house: ")
    patronas = input("patronas: ")
    return Student(name, house, patronas)


if __name__ == "__main__":
    main()
