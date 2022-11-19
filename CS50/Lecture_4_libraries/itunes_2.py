import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=10&term="
    + sys.argv[1]
)

dict_1 = response.json()["results"]

for i in dict_1:
    print(i["trackName"])

# print(response.json()["results"][0]["trackName"])
