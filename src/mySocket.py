import socket
from settings import HOST, PORT, PASS, LOGIN_ID, CHANNEL_ID


# Opens initial connection to twitch channel with necessary credentials
def openSocket():
    global SOCKET_
    s = socket.socket()
    SOCKET_ = s
    print SOCKET_
    print s
    s.connect((HOST, PORT))

    # Login request
    s.send("PASS " + PASS + "\r\n")
    s.send("NICK " + LOGIN_ID + "\r\n")
    s.send("JOIN #" + CHANNEL_ID + "\r\n")


# Constructs message for bot to write in chat
def sendMessage(message_):
    s = SOCKET_
    message = str(message_)
    result = "PRIVMSG #" + CHANNEL_ID + " :" + message
    s.send(result + "\r\n")
    print("Sent: " + result)

# Constructs message for Twitch servers
def sendCommand(message_):
    s = SOCKET_
    message = str(message_)
    s.send(message + "\r\n")

def updateBuffer(buffer):
    s = SOCKET_
    return buffer + s.recv(1024)