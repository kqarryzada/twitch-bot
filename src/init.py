import string
from mySocket import *

def initial():
    openSocket()
    joinRoom()

# Performs chat initialization
def joinRoom():
    buffer = ""
    Loading = True
    while Loading:
        buffer = updateBuffer(buffer)
        strip_queue = string.split(buffer, "\n")
        buffer = strip_queue.pop()

        for line in strip_queue:
            print(line)
            Loading = loadingComplete(line)

    sendMessage("Successfully joined chat.")


# Checks for end of string message
def loadingComplete(line):
    if "End of /NAMES list" in line:
        return False
    else:
        return True
