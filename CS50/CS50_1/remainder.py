# it seems like the if condition is satisfied if you pass it the boolean value "True"
def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("even")
    else:
        print("odd")

# use the modulus operator (%) to spit out the remainder of the division. If the remained is 0, it must be even
def is_even(n):
    return n % 2 == 0

main()
