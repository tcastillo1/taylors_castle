import sys

# this checks the length of the sys.argv list. If the list only has 1 item in it (the program name),
# then we know a name hasn't been provided, so we will use John Doe instead
if len(sys.argv) == 1:
    x = "John Doe"
else:
    x = sys.argv[1]

print("Hello, my name is ",
      x,
      ", this program is called: ",
      sys.argv[0],
      sep=""
      )
