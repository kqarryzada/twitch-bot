import string

# Extracts username & message from broadcaster's chat
def getUserAndMsg(line):
    if line == "":
        print "\n\n\n\nEmpty string entered into getUserAndMsg()\n\n\n\n"
        return None

    separate = line.split(":", 2)
    seg = separate[1]
    message = separate[2]

    # seg now contains [username]![other junk], so extract
    seg2 = seg.split("!", 1)
    username = seg2[0]
    
    return username, message