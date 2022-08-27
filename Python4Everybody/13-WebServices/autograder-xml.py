"""
Task:
    Write a program that will prompt for a URL, read the XML data from that URL 
    using urllib and then parse and extract the comment counts from the XML 
    data to compute the sum of the numbers in the file.

    The XML data will have the following format:

    <comment>
        <name>Matthias</name>
        <count>97</count>
    </comment>

    To make the code a little simpler, you can use an XPath selector string to 
    look through the entire tree of XML for any tag named 'count' with the 
    following line of code:

    counts = tree.findall('.//count')

Version:
    0.2.2
"""
# import modules
import urllib.request as urlReq
import xml.etree.ElementTree as ET

# read data from URL
data = ""
while True:
    url = input("Enter URL for XML document: ")
    try:
        data = urlReq.urlopen(url).read()
        break
    except:
        print("ERROR - could not open page")

# create object list of count tags in data
lst = (ET.fromstring(data).findall('.//count'))

# iterate list to extract integer information
for x in range(len(lst)):
    lst[x] = int(lst[x].text)

# print sum
print(sum(lst))