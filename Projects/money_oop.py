class time_value:
    def __init__(self, rate, time, units):
        self.units = "y"
        self.rate = 0.03
        self.time = 5
        return self.rate * self.time

    # def __str__(self):
    #     return f"{self.rate} {self.time}"


def main():
    amount = input()
    future_value = amount * (time_value.rate + 1) ** time_value.time
    print(future_value)


if __name__ == "__main__":
    main()
