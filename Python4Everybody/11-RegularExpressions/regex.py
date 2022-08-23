"""
Task:
    Use regex to find all of the numbers in the text and compute the sum of 
    these numbers. For now, I am assuming these numbers are Ints.

version:
    0.2.3
"""
import re

# load file
while True:
    file = input("Please enter filename: ")
    try:
        fhandle = open(file)
        break
    except:
        print("Could not find file", file)

# find and sum numbers
total = 0

for line in fhandle:
    nums = re.findall('[0-9]+', line)
    for num in nums:
        total += int(num)

print(total)
