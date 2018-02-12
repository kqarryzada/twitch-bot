import string
from mySocket import openSocket, sendMessage
from init import joinRoom
from chat import chatMsgHandler

def pingCheck(s, line):
    if line == "PING :tmi.twitch.tv":
        print "Twitch sent ping request. Ready to pong"
        s.send("PONG :tmi.twitch.tv")

if __name__ == "__main__":
    s = openSocket()
    joinRoom(s)

    buffer = ""

    while True:
        buffer = buffer + s.recv(1024)
        strip_queue = string.split(buffer, "\n")
        buffer = strip_queue.pop()

        for line in strip_queue:
            print "\nNew line in strip_queue: ", line

            # Check to make sure twitch hasn't checked the bot is AFK
            pingCheck(s, line)

            chatMsgHandler(line)
else:
    print "Error: Could not start program.\n\n"
