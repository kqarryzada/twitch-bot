# import requests
import string
from mySocket import sendMessage

def casual(user):
    retMsg = user + \
        "  http://i0.kym-cdn.com/photos/images/original/000/625/834/a48.png"
    sendMessage(retMsg)

def config(user):
    retMsg = user + " cfg will be added soon!"
    sendMessage(retMsg)

def commands(user, cmdList):
    retMsg = user + " List of commands: "

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

def source(user):
    retMsg = user + (" The source code for this bot is located at: "
        "https://github.com/kqarryzada/twitch-bot")

def uptime(user):
    # retMsg = user
    retMsg = "Uptime not implemented yet"

    sendMessage(retMsg)
