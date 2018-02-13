import pdb
import string

# Project files
import settings
from mySocket import updateBuffer, sendCommand
from init import initial
from chat import chatMsgHandler

def pingCheck(line):
    # pdb.set_trace()
    if line == "PING :tmi.twitch.tv\r":
        print "Twitch sent ping request. Ready to pong"
        sendCommand("PONG :tmi.twitch.tv")
        return True

    return False

if __name__ == "__main__":
    initial()
    buffer = ""

    while True:
        buffer = updateBuffer(buffer)
        strip_queue = string.split(buffer, "\n")
        buffer = strip_queue.pop()

        for line in strip_queue:
            print "\nNew line in strip_queue: ", line

            # Check to make sure twitch hasn't checked the bot is AFK
            pChk = pingCheck(line)
            if pChk:
                continue    # Line has been evaluated, move to next

            chatMsgHandler(line)
else:
    print "Error: Could not start program.\n\n"
