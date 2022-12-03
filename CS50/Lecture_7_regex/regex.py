# regular expressions
import re

email = "fake_email.fake@gmail.com"

# ^ start with
# [^] excludes
# [] includes
# $ ends with
# . 1 or more of the following character
# \w any set of letters or numbers and underscores
# \W no letters or numbers or underscores
# \s whitespace allowed
# \S no whitespace allowed
if re.search("^[\w.]+@+[\w]+\.com$", email, flags=re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# if re.search("^fa+[^@ ]+@+[^@ ]+\.com$", email):
#     print("Valid")
# else:
#     print("Invalid")
