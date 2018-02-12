import socket
from settings import HOST, PORT, PASS, LOGIN_ID

def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))

    # Login request
    s.send("PASS " + PASS + "\r\n")
    s.send("NICK " + LOGIN_ID + "\r\n")