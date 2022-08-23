"""
Task:
    Write a program to look for lines of the form:

    New Revision: 39772

    Extract the number from each of the lines using a regular expression and the 
    findall() method. Compute the average of the numbers and print out the 
    average as an integer.

version:
    0.2.15
"""
import re


import re

# open file
file = open("mbox.txt").read()

# build list of data with regex
count = [   int(n) for n in 
            re.findall("^New Revision: ([0-9]+)", file, re.MULTILINE) ]

# print result
print(sum(count)//len(count))