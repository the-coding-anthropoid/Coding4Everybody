"""
Task:
    Write a Python program similar to http://www.py4e.com/code3/urllink2.py. The 
    program will use urllib to read the HTML from the data files below, and 
    parse the data, extracting numbers and compute the sum of the numbers in the 
    file using BeautifulSoup
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# get data
url = input("Enter URL: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span elements
tags = soup("span")

# sum contents of tags
total = 0
for tag in tags:
    total += int(tag.contents[0])

# output
print(total)