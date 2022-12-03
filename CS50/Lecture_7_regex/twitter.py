import re

url = "http://www.twitter.com/my_username"

# splitting the url out into 3 parts. i think it would be better to split into 2 but this is fine for clarity
extract_username = re.search(r"(.*)+(.com/)+(.*$)", url)

# it seems like the "groups" method will print all groups where as the group function requires the number
print("all groups: ",  extract_username.groups())

# extract the username:
print("extract the third group:", extract_username.group(3))
