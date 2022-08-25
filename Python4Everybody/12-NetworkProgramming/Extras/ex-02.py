"""
Task:
    Change your socket program so that it counts the number of characters it has 
    received and stops displaying any text after it has shown 3000 characters. 
    The program should retrieve the entire document and count the total number 
    of characters and display the count of the number of characters at the end 
    of the document.

Version:
    0.2.5
"""

import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = "http://data.pr4e.org/romeo-full.txt"
soc.connect((url.split('/')[2], 80))
soc.send(("GET " + url + " HTTP/1.0\r\n\r\n").encode())

count = 0

while True:
    data = soc.recv(1)
    if len(data) == 0:
        break
    else:
        count += 1
        if count <= 3000:
            print(data.decode(), end='')

print("\nDisplaying 3000 out of", count, "characters")
