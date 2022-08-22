"""
Task:
     Write a program to read through a mail log, build a histogram using a 
     dictionary to count how many messages have come from each email address, 
     and print the dictionary.

version:
    0.1.2
"""

# create dictionary to hold data
count = {}
# open file
fhandle = open("mbox-short.txt")

for line in fhandle:
    # find correct lines
    if line.startswith("From "):
        # get email from correct line
        email = line.split()[1]
        # add email to histogram
        count[email] = count.get(email, 0) + 1

print(count)