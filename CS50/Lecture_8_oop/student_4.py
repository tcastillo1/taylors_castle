class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name

    @classmethod
    def get(cls):
        cls.name = input("name: ")
        return cls.name


class House:


class Subject:


def main():
    wizard = Wizard.get()


if __name__ == "__main__":
    main()
