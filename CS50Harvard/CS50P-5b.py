## cowsay exercise ##

# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.trex("hello, " + sys.argv[1])


## request exercise ##

# import requests
# import sys
# import json

# if len(sys.argv) != 2:
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# # after the = in the quotes the artist name so we type python CS50P-5b.py in the terminal and then artist name and execute
# # that will search the artist name in the database
# print(json.dumps(response.json(), indent=2))      # this ensures the output that we get is in JSON because it is suppose to be in JSON.
# # json.dump helps with formatting because response.json converts api to a python dictionary(looks ugly) and then json.dumps
# # converts it back to a formatted JSON(look presentable)


## request exercise but w/ searching for trackname ##

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])     # Will filter our the tracknames!
