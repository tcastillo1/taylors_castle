import datetime


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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.annual_raise = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


class Developer(Employee):
    annual_raise = .08

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_emp(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        x = 1
        for i in self.employees:
            print(f"{x}. {i.fullname()}")
            x = x + 1


employee_1 = Employee("Timmy", "Lincecum", 100000000)
employee_2 = Developer("Jimmy", "Lincecum", 100000000, "python")
manager_1 = Manager("Dusty", "Baker", 300000000, [employee_1, employee_2])

manager_1.print_employees()
employee_1.apply_raise()
employee_2.apply_raise()

print(employee_1.pay)
print(employee_2.pay)

# employee_2 = Employee("Randy", "Johnson", 50000000)
