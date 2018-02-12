import socket
from settings import HOST, PORT, PASS, LOGIN_ID, CHANNEL_ID

# Opens initial connection to twitch channel with necessary credentials
def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))

    # Login request
    s.send("PASS " + PASS + "\r\n")
    s.send("NICK " + LOGIN_ID + "\r\n")
    s.send("JOIN #" + CHANNEL_ID + "\r\n")
    return s


# Constructs message for bot to write in chat
def sendMessage(s, message):
	result = "PRIVMSG #" + CHANNEL_ID + " :" + message
	s.send(result + "\r\n")
	print("Sent: " + result)