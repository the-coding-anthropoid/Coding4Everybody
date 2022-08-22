"""
Task:
    Write a program that categorizes each mail message by which day of the week 
    the commit was done. To do this look for lines that start with “From ”, then 
    look for the third word and keep a running count of each of the days of the 
    week. At the end of the program print out the contents of your dictionary 
    (order does not matter).

version:
    0.1.3
"""

# dict to hold histogram
count = {}
# open file
fhandle = open("mbox-short.txt")

for line in fhandle:
    # find correct lines
    if line.startswith("From "):
        # get day from line
        day = line.split()[2]
        # add day to histograms
        count[day] = count.get(day, 0) + 1

print(count)