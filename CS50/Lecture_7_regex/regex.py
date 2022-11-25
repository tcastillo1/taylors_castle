# regular expressions
import re

email = "tcastillo1@gmail.com"

if re.search("^t" + ".*@.*" + "com$", email):
    print("Valid")
else:
    print("Invalid")
