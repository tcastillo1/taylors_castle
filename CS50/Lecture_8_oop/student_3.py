class Student():
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("name: ")
        house = input("house ")
        return cls(name, house)


def main():
    # this allows you to supply the name and house as arguments rather than inputs
    print(Student("Harry", "Gryffindor"))
    # this allows you to call the Student object and then input the name and house
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
