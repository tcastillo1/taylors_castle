class Vehicle:
    def __init__(self, max_speed, mpg):
        self.max_speed = max_speed
        self.mpg = mpg

    def __str__(self):
        return f"This vehicle has a max speed of {self.max_speed} mph and gets {self.mpg} mpg"


class Bus(Vehicle):
    def __init__(self, max_speed, mpg):
        super().__init__(max_speed, mpg)

    def __str__(self, max_speed, mpg):
        super().__init__(max_speed, mpg)
        return f"This bus has a max speed of {self.max_speed} mph and gets {self.mpg} mpg"


ford_focus = Vehicle(95, 33)
bus = Bus(80, 45)
print(ford_focus)
print(bus)
