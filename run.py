import string
from mySocket import openSocket, sendMessage
from init import joinRoom
from read import getUserAndMsg

s = openSocket()
joinRoom(s)

buffer = ""

def pingCheck(s, line):
    if line == "PING :tmi.twitch.tv":
        print "Twitch sent ping request. Ready to pong"
        s.send("PONG :tmi.twitch.tv")
    
def chatMsgHandler(line):
    user = ""
    message = ""
    user, message = getUserAndMsg(line)
    print user + " said: " + message

    # if message[0] == '!'


while True:
    buffer = buffer + s.recv(1024)
    strip_queue = string.split(buffer, "\n")
    buffer = strip_queue.pop()

    for line in strip_queue:
        print "\nNew line in strip_queue: ", line

        # Check to make sure twitch hasn't checked the bot is AFK
        pingCheck(s, line)

        chatMsgHandler(line)
        
