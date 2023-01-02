class Employee:

    annual_raise = .04
    number_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@gmail.com"
        Employee.number_of_employees += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * (1 + self.annual_raise))


employee_1 = Employee("Timmy", "Lincecum", 100000000)
employee_1.apply_raise()
employee_2 = Employee("Randy", "Johnson", 50000000)
print(Employee.annual_raise)
print(employee_1.annual_raise)
print(Employee.number_of_employees)

# note these produce the same result. The first line of code is an instance of Employee.
# The second line of code doesnt know which instance to run which is why we have to provide it (employee_1)
# print(employee_1.fullname())
# print(Employee.fullname(employee_1))
