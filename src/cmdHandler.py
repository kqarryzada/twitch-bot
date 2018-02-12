import string
from mySocket import sendMessage
def casual(user):
    retMsg = "@" + str(user),  \
        "http://i0.kym-cdn.com/photos/images/original/000/625/834/a48.png"
    sendMessage(retMsg)

def config(user):
    retMsg = "@" + str(user), \
        "cfg will be added soon!"
    sendMessage(retMsg)

def commands(user, cmdList):
    retMsg = "@" + str(user), \
        "List of commands:"

    lastIndex = len(cmdList) - 1
    for str in range(len(cmdList)):
        # Perform integer checks for string manip. efficiency
        if i != lastIndex:
            retMsg = retMsg + cmdList[i] + ", "
        else:
            retMsg = retMsg + cmdList[i]
    sendMessage(retMsg)

def deserve(user):
    retMsg = "@" + str(user), \
        "https://pbs.twimg.com/media/CZcrKQ6WEAQarVy.jpg"
    sendMessage(retMsg)


def hud(user):
    retMsg = "@" + str(user), \
        "https://github.com/rbjaxter/budhud/"
    sendMessage(retMsg)

def logs(user):
    # retMsg = "@" + str(user)
    print "Logs not implemented yet"

def uptime(user):
    # retMsg = "@" + str(user)
    print "Uptime not implemented yet"

def viewmodels(user):
    retMsg = "@" + str(user), \
        "https://www.youtube.com/watch?v=4phrSBGD1qA"
    sendMessage(retMsg)