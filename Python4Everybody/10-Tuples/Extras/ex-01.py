"""
Task:
    Write a program to read and parse the “From” lines and pull out the addresses 
    from the line. Count the number of messages from each person using a 
    dictionary. After all the data has been read, print the person with the most 
    commits by creating a list of (count, email) tuples from the dictionary. 
    Then sort the list in reverse order and print out the person who has the 
    most commits.

version:
    0.3.4
"""

# load file
from audioop import reverse


while True:
    file = input("Enter file name: ")
    try:
        fhandle = open(file)
        break
    except:
        print("could not find", file, "please try again...")

# parse address from "From " lines; put in dictionary
count = dict()
for line in fhandle:
    if line.startswith("From "):
        address = line.split()[1]
        count[address] = count.get(address, 0) + 1

# sort and print most commits
mostCommits = sorted(   [ (count, email) for email, count in count.items()],
                        reverse=True)[0]
print(mostCommits[1], mostCommits[0])