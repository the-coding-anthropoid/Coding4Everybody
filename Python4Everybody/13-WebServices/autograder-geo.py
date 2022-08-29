"""
Task:
    Write a program that will prompt for a location, contact a web service and 
    retrieve JSON for the web service and parse that data, and retrieve the 
    first place_id from the JSON. A place ID is a textual identifier that 
    uniquely identifies a place as within Google Maps.

Version:
    0.1.3
"""
import urllib.request, urllib.parse
import json

# set params for json queery
params = dict()
params["address"] = input("Address: ")
params["key"] = 42

# get data from server
url = "http://py4e-data.dr-chuck.net/json?" + urllib.parse.urlencode(params)
# parse data
data = json.loads(urllib.request.urlopen(url).read().decode())

# print output
print(data["results"][0]["place_id"])

