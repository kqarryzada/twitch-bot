import string

from cmdHandler import *
from jsonRequests import getJSON
from read import getUserAndMsg

cmdList = ["!casual", "!cfg",  "!commands", "!config", "!deserve", "!help", \
            "!hud", "!sourcecode", "!uptime"]

# Sanity check to prevent errors if an incorrect insertion occurs
def chatInit():
    cmdList.sort()  

def chatMsgHandler(line):
    # getUserAndMsg() returns a tuple. Will have to convert to 
    # individual strings.
    user_tuple = ""
    message_tuple = ""
    user_tuple, message_tuple = getUserAndMsg(line)

    user = "".join(user_tuple)
    user = "@" + user
    message = "".join(message_tuple)
    
    print user + " said: " + message

    if message == "!check":
        response = getJSON()
        print response
        return

    # Command has been executed
    if message[0] == '!':
        stringSeg = message.split(None, 1)

        # Make typing commands case-insensitive
        firstWord = stringSeg[0].lower()
        ID = findCmdID(firstWord)

        # If user types something like "!hud @OtherTwitchUser", we should
        # tag OtherTwitchUser instead of the one who typed the command.
        # But first, check stringSeg[1] exists.
        if len(stringSeg) > 1:      
            if stringSeg[1][0] == '@':
                # Extract username and tag them instead
                newUser = stringSeg[1].split(None, 1)
                user = newUser[0]
        
        execCmd(ID, user)


# Performs binary search on cmd list and returns the associated index.
# Returns -1 upon failure
def findCmdID(string_):
    found = False
    lastIndex = len(cmdList) - 1
    
    # Don't bother searching the list if it's already out of bounds
    if string_ < cmdList[0] or string_ > cmdList[lastIndex]:
        return -1
    
    # Initialize indeces for search, i.e., 3 "pointers"
    leftBound = 0
    rightBound = lastIndex
    
    # Need to set ptr as midpoint between rB & lB, which is:
    # ((rightBound - leftBound) / 2) + leftBound
    #
    # This evaluates to: (rightBound + leftBound) / 2
    ptr = (rightBound + leftBound) / 2

    while True:
        # Grab element
        testWord = cmdList[ptr]
        if string_ == testWord:
            found = True
            break
        
        elif string_ < testWord:
            rightBound = ptr

        else:
            leftBound = ptr

        ptr = (rightBound + leftBound) / 2      # Update ptr after checks
        if ptr == leftBound or ptr == rightBound:
            # This code runs when checking either extreme of the list
            leftCheck = (string_ == cmdList[leftBound])
            if leftCheck:
                ptr = leftBound
                found = True

            rightCheck = (string_ == cmdList[rightBound])
            if rightCheck:
                ptr = rightBound
                found = True
            break

    # Check upon exiting loop in case word is at either extreme of the list
    if string_ == cmdList[ptr]:
        found = True

    if found == True:
        return ptr
    else:
        return -1

def execCmd(ID, user):
    if ID < 0 or ID > (len(cmdList) - 1):
        errStr = ("\n\n---------------------------------------\n"
            "Error: Invalid ID passed into execCmd()\n"
            "---------------------------------------\n\n")
        print errStr

    if ID == 0:
        casual(user)
    elif ID == 1:
        config(user)
    elif ID == 2:
        commands(user, cmdList)
    elif ID == 3:
        config(user)
    elif ID == 4:
        deserve(user)
    elif ID == 5:
        commands(user, cmdList)      # For now, "!help" just lists commands.
    elif ID == 6:
        hud(user)
    elif ID == 7:
        source(user)
    elif ID == 8:
        uptime(user)
