class Employee:

    annual_raise = .04
    number_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = f"{self.first}.{self.last}@gmail.com"
        Employee.number_of_employees += 1

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"


employee_1 = Employee("Timmy", "Lincecum", 100000000)

print(employee_1.fullname)
print(employee_1.email)


employee_1.first = "Bobby"

# the email is not updating!! getter and setters can fix this?
print(employee_1.fullname)
print(employee_1.email)


# employee_2 = Employee("Randy", "Johnson", 50000000)
