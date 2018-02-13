import pdb
import string
from mySocket import sendMessage
def casual(user):
    # pdb.set_trace()
    retMsg = user + \
        "  http://i0.kym-cdn.com/photos/images/original/000/625/834/a48.png"
    sendMessage(retMsg)

def config(user):
    retMsg = user + \
        " cfg will be added soon!"
    sendMessage(retMsg)

def commands(user, cmdList):
    retMsg = user + \
        " List of commands: "

    lastIndex = len(cmdList) - 1
    for strIndex in range(len(cmdList)):
        # Perform integer checks for string manip. efficiency
        if strIndex != lastIndex:
            retMsg = retMsg + cmdList[strIndex] + ", "
        else:
            retMsg = retMsg + cmdList[strIndex]
    sendMessage(retMsg)

def deserve(user):
    retMsg = user + \
        " https://pbs.twimg.com/media/CZcrKQ6WEAQarVy.jpg"
    sendMessage(retMsg)


def hud(user):
    retMsg = user + \
        " I use BudHud. Download it here: https://github.com/rbjaxter/budhud/"
    sendMessage(retMsg)

def logs(user):
    #  retMsg = user +    
    retMsg = "Logs not implemented yet"
    sendMessage(retMsg)

def uptime(user):
    #  retMsg = user +    
    retMsg = "Uptime not implemented yet"
    sendMessage(retMsg)

def viewmodels(user):
    retMsg = user + \
        (" I use Yttrium's viewmodels, which allows you to hide certain "
        "items and show others. Installation tutorial here: "
        "https://youtu.be/4phrSBGD1qA")
    sendMessage(retMsg)