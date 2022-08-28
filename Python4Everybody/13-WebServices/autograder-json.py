"""
Task:
    Write a program that will prompt for a URL, read the JSON data from that URL 
    using urllib and then parse and extract the comment counts from the JSON 
    data to compute the sum of the numbers in the file.

    The JSON data will have the following format:

    {
        comments: [
            {
                name: "Matthias"
                count: 97
            },
            {
                name: "Geomer"
                count: 97
            }
            ...
        ]
    }

Version:
    0.3.1
"""
import urllib.request as urlReq
import json

# get data from URL and transpose into dict
url = input("URL: ")
data = json.loads(urlReq.urlopen(url).read())

# extract and sum comments
count = 0

for item in data["comments"]:
    count += int(item["count"])

# output
print(count)