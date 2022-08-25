"""
Task:
    Replicate the functionality of ex-02.py, this time using urllib. Do not 
    worry about the header information.

Version:
    0.2.3
"""

import urllib.request

file = urllib.request.urlopen('http://data.pr4e.org/romeo-full.txt')

count = 0

for line in file:
    line = line.decode().strip() + '\n'
    for character in line:
        count += 1
        if count <= 3000:
            print(character, end='')

print("\n\nShowing 3000 out of", count, "characters")