import string
from read import getUserAndMsg

# THIS LIST MUST BE SORTED ALPHABETICALLY
cmdList = ["cfg", "config", "commands", "help", "uptime"]

def chatMsgHandler(line):
    user = ""
    message = ""
    user, message = getUserAndMsg(line)
    print user + " said: " + message

    # Command has been executed
    if message[0] == '!':
        # execCmd(user, message)


#def execCmd(user, message):

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
            rightCheck = (string_ == cmdList[rightBound])
            found = leftCheck or rightCheck
            break

    # Check upon exiting loop in case word is at either extreme of the list
    if string_ == cmdList[ptr]:
        found = True

    if found == True:
        return ptr
    else:
        return -1