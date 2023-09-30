#The differences in follower data are found by comparing the data of
#two different JSON files. This file makes the process possible,

import json #Fetching the data

## Importing the Values class ##
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from variables.values import Values
################################

def getJsonData(jsonDataFileName):
    jsonDataFile = open(jsonDataFileName, "r")
    jsonContent = json.load(jsonDataFile)
    return jsonContent


def compareFollowerLists():
    values = Values()
    #Next up we will wrap up all the usernames from the old followers list and
    #iterate the new list by checking if its names are on the old list as well.
    #If they are, they have been following for some time and are still following.
    #If someone isn't on the old list, but is on the new one, it means they
    #have started following. If it's the other way around, they've unfollowed.
    oldFollowerData = getJsonData(values.OLD_JSON_FILE)["content"][1]["usernames"]
    newFollowerData = getJsonData(values.NEW_JSON_FILE)["content"][1]["usernames"]

    unfollowedList = []
    followedList = []

    for username in newFollowerData:
        isOldFollower = False
        for oldUsername in oldFollowerData:
            if oldUsername == username:
                isOldFollower = True
        #If the user is not in the old data list, they're a new follower
        if not isOldFollower:
            followedList.append(username)

    for oldUsername in oldFollowerData:
        hasUnfollowed = True
        for username in newFollowerData:
            if username == oldUsername:
                hasUnfollowed = False
        if hasUnfollowed:
            unfollowedList.append(oldUsername)
    
    return [followedList, unfollowedList]



    

    
