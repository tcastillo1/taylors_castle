import sys

# this checks the length of the sys.argv list. If the list only has 1 item in it (the program name),
# then we know a name hasn't been provided, so we will use John Doe instead
try:
    print("Hello, my name is ",
          sys.argv[1],
          ", this program is called: ",
          sys.argv[0],
          sep=""
          )
except IndexError:
    print("Hello, my name is John Doe",
          ", this program is called: ",
          sys.argv[0],
          sep=""
          )
