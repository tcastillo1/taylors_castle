
def conversion(string):
    # string = input("gimme a smiley or sad face--> ")
    if string == ":)":
        smiley = "Hello! 🙂"
    elif string == ":(":
        smiley = "Goodbye 🙁"
    else:
        smiley = "error"
    print(smiley)
    
conversion(":)")