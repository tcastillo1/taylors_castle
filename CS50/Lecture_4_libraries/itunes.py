import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term="
    + sys.argv[1]
)

# response.json() is returning a dictionary
print("")
print("response.json() is returning a dictionary:")
print("")
print(response.json())
print("####################################################")
print("")

# lets access the 2nd key value pair of results
print("lets access the 2nd key value pair of the dictionary")
print("this returns a list with 1 item. The single item is itself a dictionary.")
print("")
print(response.json()["results"])
print("####################################################")
print("")


# lets return the first item of the list (which is a dictionary)
# all this does is strip the list down to a dictionary
# it seems odd that a list only has 1 dictionary in it. It seems pointless. Why not just return a dictionary instead of a 1 item
# list with a dictionary??? This is because if we remove the limit = 1 restriciton, the api can return much more than 1 dictionary.
print("lets return the first item of the list. this essentially just strips the list off")
print("")
print(response.json()["results"][0])
print("####################################################")
print("")


# now that we have a dictionary, lets pull the "trackName" key value pair
print("now that we have a dictionary, lets pull the 'trackName' key value pair")
print(response.json()["results"][0]["trackName"])
