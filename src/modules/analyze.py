"""
The differences in follower data are found by comparing the data of
two different JSON files.
"""

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import modules.json_data as json_data
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from variables.values import Values


def compareFollowerLists() -> list:
    """ Finding out who has followed and who has unfollowed

    Returns:
        [followedList, unFollowedList] (list): A list consisting of two lists: 
            1. A list that contains the new followers
            2. A list that contains the ones that have unfollowed
    """
    try:
        values = Values()

        #We'll append the users who have followed/unfollowed to two lists
        unfollowedList = []
        followedList = []

        #Fetching data from followerdata.json and oldfollowerdata.json
        oldFollowerData = json_data.getJsonData(values.OLD_JSON_FILE)["content"][1]["usernames"]
        newFollowerData = json_data.getJsonData(values.NEW_JSON_FILE)["content"][1]["usernames"]

        #Finding the new followers
        for username in newFollowerData:
            isOldFollower = False

            for oldUsername in oldFollowerData:
                #Checking if the username is in both data lists
                if oldUsername == username:
                    isOldFollower = True
            if not isOldFollower:
                followedList.append(username)

        #Finding the ones who have unfollowed
        for oldUsername in oldFollowerData:
            hasUnfollowed = True

            for username in newFollowerData:
                if username == oldUsername:     #A match ==> the user is still a follower
                    hasUnfollowed = False

            if hasUnfollowed:
                unfollowedList.append(oldUsername)

    except Exception as exception:
        print(values.EXCEPTION_DEFAULT + str(exception))
        
    return [followedList, unfollowedList]

    

    
