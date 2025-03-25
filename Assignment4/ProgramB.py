# Program Name: ProgramB.py
# Course: IT3883/Section 17540
# Student Name: Kalyb Sanders
# Assignment Number: 4
# Due Date: 03/ 24/ 2025
# Purpose: This program establishes a connection between two computers. The first computer (Program A)
# inputs a string to send to the second computer (ProgramB), when B receives this message, it
# sets the entire string to upper case and sends it back to A.
#
# List Specific resources used to complete the assignment.
#   I used the reading provided in the class

import socket

# create a socket and establish connection to 127.0.0.1 (localhost) on port 40210
s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
s.connect(("127.0.0.1", 40210))

# receive message from A.
received_msg = s.recv(256).decode('utf-8')

# set the message to uppercase
uppercase_msg = received_msg.upper()
uppercase_encoded = uppercase_msg.encode('utf-8')

print("converting received message to uppercase: \n" + received_msg + " -----> " + uppercase_msg)

# send the message back on the socket to A.
s.sendall(uppercase_encoded)

# print the socket close message
print(s.recv(256).decode('utf-8'))

# close the program
s.close()