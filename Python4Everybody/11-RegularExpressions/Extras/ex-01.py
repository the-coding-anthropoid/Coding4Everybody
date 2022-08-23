"""
Task:
    Write a simple program to simulate the operation of the grep command on 
    Unix. Ask the user to enter a regular expression and count the number of 
    lines that matched the regular expression

version:
    0.4.2
"""
import re


#open file
while True:
    file = input("Enter file to parse: ")
    try:
        fhandle = open(file)
        break
    except:
        print("Could not find file", file)

# get regex
regex = input("Enter regular expression to search for: ")

# count lines
lineCount = 0
for line in fhandle:
    if re.search(regex, line):
        lineCount += 1

# output
print(  "The file", file, "contained", lineCount,
        "lines that matched the regular expression '" + regex + "'")