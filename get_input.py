import json
import requests
import sys
import os

script_directory = os.path.dirname(os.path.abspath(__file__))

year, day = sys.argv[1:3]

cookiefile = open(os.path.join(script_directory, "cookie.json"), "r")
cookies = json.loads(cookiefile.read())
cookiefile.close()

response = requests.get(
    "https://adventofcode.com/" + year + "/day/" + day + "/input", cookies=cookies
)

inputfile = open(
    os.path.join(script_directory, year, "inputd" + ("0" + day)[-2:] + ".txt"), "w"
)
inputfile.write(response.text)
inputfile.close()
