# Program Name: ProgramA.py
# Course: IT3883/Section 17540
# Student Name: Kalyb Sanders
# Assignment Number: 4
# Due Date: 03/ 24/ 2025
# Purpose: This program establishes a socket connection between two computers. The first computer (Program A)
# inputs a string to send to the second computer (ProgramB), when B receives this message, it
# sets the entire string to upper case and sends it back to A.
#
# List Specific resources used to complete the assignment.
#   I used the reading provided in the class

import socket

# create a socket. Bind and listen on 127.0.0.1 (localhost) on port 40210
s = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
s.bind(("127.0.0.1", 40210))
s.listen()
conn, addr = s.accept()  # Blocks

# send a message to program B.
msg = input("Input a string to send: ").encode('utf-8')
conn.sendall(msg)

# receive message from B (should be the entered message in upper case).
new_msg = conn.recv(256).decode('utf-8')

# print the new message from B
print(new_msg)

# close the socket.
conn.sendall(b'Closing connection...')
s.close()