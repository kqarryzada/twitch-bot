import string
import pdb

from cmdHandler import *
from read import getUserAndMsg

cmdList = ["!casual", "!cfg",  "!commands", "!config", "!deserve", "!help", \
            "!hud", "!log", "!logs", "!uptime", "!viewmodels"]

# Sanity check to prevent errors if an incorrect insertion occurs
def chatInit():
    cmdList.sort()  

def chatMsgHandler(line):
    # getUserAndMsg() returns a tuple. Will later have to convert to 
    # individual strings.
    user_tuple = ""
    message_tuple = ""
    user_tuple, message_tuple = getUserAndMsg(line)

    # pdb.set_trace()

    user = "".join(user_tuple)
    message = "".join(message_tuple)
    
    print user + " said: " + message

    # Command has been executed
    if message[0] == '!':
        stringSeg = message.split(None, 1)
        firstWord = stringSeg[0]
        ID = findCmdID(firstWord)
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

    # pdb.set_trace()

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
        logs(user)
    elif ID == 8:
        logs(user)
    elif ID == 9:
        uptime(user)
    elif ID == 10:
        viewmodels(user)
    