"""
Task:
    Start at: http://py4e-data.dr-chuck.net/known_by_Roxy.html. Find the link at 
    position 18 (the first name is 1). Follow that link. Repeat this process 7 
    times. The answer is the last name that you retrieve.
    Hint: The first character of the name of the last page that you will load 
    is: R
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# get data
url = input("Initial URL: ")
position = int(input("Link position: ")) - 1
repeat = int(input("Links in URL chain: ")) + 1

# loop through urls
for x in range(int(repeat)):
    html = urllib.request.urlopen(url).read()
    print("Retrieving:", url)
    soup = BeautifulSoup(html, "html.parser")
    url = soup('a')[position].get('href', None)