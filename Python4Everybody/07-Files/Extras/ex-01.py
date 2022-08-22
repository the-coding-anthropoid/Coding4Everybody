"""
Task:
     Write a program to read through a file and print the contents of the file 
     (line by line) all in upper case.

Version:
    0.1.2
"""

# open file
fhand = open("mbox-short.txt")
# for each line
for line in fhand :
    # print line; as upper case; remove extraneous '/n'
    print(line.upper().rstrip())