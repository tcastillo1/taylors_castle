
def conversion(stringy):
    # string = input("gimme a smiley or sad face--> ")
    if stringy == ":)":
        smiley = "Hello! 🙂"
    elif stringy == ":(":
        smiley = "Goodbye 🙁"
    else:
        smiley = "error"
    print(smiley)


conversion(":(")
