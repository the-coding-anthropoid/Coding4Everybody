"""
Task:
     Write a program to read through a mail log, build a histogram using a 
     dictionary to count how many messages have come from each domain name, 
     and print the dictionary.

version:
    0.2.1
"""

# dictionary to hold data
count = {}
# open file
fhandle = open("mbox-short.txt")

#create histpgram
for line in fhandle:
    if line.startswith("From "):
        domain = line.split()[1].split('@')[1]
        count[domain] = count.get(domain, 0) +1

print(count)