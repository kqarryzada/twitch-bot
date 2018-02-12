import string
from mySocket import sendMessage

# s is a socket
def joinRoom(s):
    buffer = ""
    Loading = True
    while Loading:
        buffer = buffer + s.recv(1024)
        strip_queue = string.split(buffer, "\n")
        buffer = strip_queue.pop()

        for line in strip_queue:
            print(line)
            Loading = loadingComplete(line)

    sendMessage(s, "Successfully joined chat.")


def loadingComplete(line):
    if "End of /NAMES list" in line:
        return False
    else:
        return True