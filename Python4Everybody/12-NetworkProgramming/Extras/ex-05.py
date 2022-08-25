"""
Task:
    (Advanced) Change the socket program so that it only shows data after the 
    headers and a blank line have been received. Remember that recv receives 
    characters (newlines and all), not lines.

version:
    0.0.0
"""

import socket

# This is using HTTP 1.0 - not all servers support the oldest protocol
# Try http://data.pr4e.org/romeo.txt if your server fails.

url = input('Enter: ')
words = url.split('/')
host = words[2]

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((host, 80))
soc.send(('GET '+url+' HTTP/1.0\r\n\r\n').encode())

count = 0
page = ""
start = 0

while True:
    data = soc.recv(512)
    if (len(data) < 1):
        break
    for x in range(len(data)):
        count += 1
        page += chr(data[x])
        if (    chr(data[x - 2]) == '\n' and 
                chr(data[x - 1]) == '\r' and
                chr(data[x]) == '\n'    ):
            start = count

print(page[start:])
print(start)

soc.close()