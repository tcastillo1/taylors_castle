score = int(input("What number grade did you get? "))

def grade():
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B not good enough!")
    else:
        print("fail")

grade()