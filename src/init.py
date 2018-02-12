import string
from mySocket import sendMessage


# Performs initial actions for connecting to chat
def joinRoom(s):
    buffer = ""
    Loading = True
    while Loading:
        # s is a socket
        buffer = buffer + s.recv(1024)
        strip_queue = string.split(buffer, "\n")
        buffer = strip_queue.pop()

        for line in strip_queue:
            print(line)
            Loading = loadingComplete(line)

    sendMessage(s, "Successfully joined chat.")


# Checks for end of string message
def loadingComplete(line):
    if "End of /NAMES list" in line:
        return False
    else:
        return True