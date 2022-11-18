def main(x, y):
    for i in range(y):
        print_row(x)


def print_row(n):
    print("#" * n, sep="")


main(5, 4)


def main2(x):
    print_square(x)


def print_square(x):
    for i in range(x):
        print("#" * x)


main2(10)
