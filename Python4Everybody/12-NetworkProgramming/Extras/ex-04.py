"""
Task:
    Change the urllinks.py program to extract and count paragraph (p) tags from 
    the retrieved HTML document and display the count of the paragraphs as the 
    output of your program. Do not display the paragraph text, only count them. 
    Test your program on several small web pages as well as some larger web 
    pages.

Version 0.2.0
"""

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# # Retrieve all of the anchor tags - old
# tags = soup('a')
# for tag in tags:
#     # Look at the parts of a tag
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)

# count <p> tags
tags = soup('p')
print(url, "has", len(tags), "<p> tags")