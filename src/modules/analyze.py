#The differences in follower data are found by comparing the data of
#two different JSON files. This file makes the process possible,

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import modules.json_data as json_data
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from variables.values import Values



def compareFollowerLists():
    """ Finding out who has followed and who has unfollowed

    Returns:
        list: A list consisting of two lists: followed & unfollowed
    """
    try:
        values = Values()
        unfollowedList = []
        followedList = []

        #Fetching data from followerdata.json and oldfollowerdata.json
        oldFollowerData = json_data.getJsonData(values.OLD_JSON_FILE)["content"][1]["usernames"]
        newFollowerData = json_data.getJsonData(values.NEW_JSON_FILE)["content"][1]["usernames"]

        for username in newFollowerData:
            isOldFollower = False

            for oldUsername in oldFollowerData:

                #Checking if the username is in both data lists
                if oldUsername == username:
                    isOldFollower = True
            if not isOldFollower:
                followedList.append(username)

        for oldUsername in oldFollowerData:
            hasUnfollowed = True

            for username in newFollowerData:
                if username == oldUsername:
                    hasUnfollowed = False
            if hasUnfollowed:
                unfollowedList.append(oldUsername)
    
    except Exception:
        print(values.EXCEPTION_DEFAULT)
        
    return [followedList, unfollowedList]



    

    
