"""
Task:
    Write a program to prompt the user for the URL so it can read any web page. 
    You can use split('/') to break the URL into its component parts so you can 
    extract the host name for the socket connect call. Add error checking using 
    try and except to handle the condition where the user enters an improperly 
    formatted or non-existent URL.

Version:
    0.1.5
"""
# create socket
import socket

while True:
    # new socket
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # prompt
    url = input("Enter URL: ")

    # resolve domain
    try:
        domain = url.split('/')[2]
    except:
        print("ERROR - improperly formatted URL")
        continue

    # connect
    try:
        mySocket.connect((domain, 80))
        break
    except:
        print("ERROR - Could not connect to domain.")
        mySocket.close()
        continue

# get document
cmd = ("GET " + url + " HTTP/1.0\r\n\r\n").encode()
mySocket.send(cmd)

# output
while True:
    data = mySocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

# close socket
mySocket.close()