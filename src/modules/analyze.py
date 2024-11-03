#------------------------------------------------------#
# Made by CaptainCluster                               #
# https://github.com/captaincluster                    #
#                                                      #
# This file contains the means to analyze the data     #
# that has been scraped                                #
#------------------------------------------------------#
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import modules.json_data as jsonData
from variables.values import Values

VALUES_INSTANCE = Values()

def compareFollowerLists() -> list:
    """ Finding out who has followed and who has unfollowed

    Returns:
        [followedList, unFollowedList] (list): A list consisting of two lists: 
            1. A list that contains the new followers
            2. A list that contains the ones that have unfollowed
    """
    try:
        unfollowedList, followedList = [], []

        oldFollowerData = jsonData.getJsonData(VALUES_INSTANCE.OLD_FOLLOWERDATA_FILE_NAME)["content"][0]["usernames"]
        newFollowerData = jsonData.getJsonData(VALUES_INSTANCE.FOLLOWERDATA_FILE_NAME)["content"][0]["usernames"]

        #Finding the new followers
        for username in newFollowerData:
            isOldFollower = False
            for oldUsername in oldFollowerData:
                #Checking if the same username is in both data lists
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
        print(VALUES_INSTANCE.EXCEPTION_DEFAULT + str(exception))
        
    return [followedList, unfollowedList]

    

    
