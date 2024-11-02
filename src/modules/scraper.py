#------------------------------------------------------#
# Made by CaptainCluster                               #
# https://github.com/captaincluster                    #
#                                                      #
# All the scraping is done here.                       #
#------------------------------------------------------#
from bs4 import BeautifulSoup
import requests
import json
import os 
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from variables.values   import Values

VALUES_INSTANCE = Values()

def getUrl() -> str:
    """Retrieving the data from username.txt file

    Returns:
        string: The url in the .txt file
    """
    userNameFile = open(VALUES_INSTANCE.FILE_USERNAME, "r", encoding="utf-8")
    gitHubUrl = userNameFile.readline() 
    gitHubFollowersUrl = f"{gitHubUrl}?tab=followers"
    return gitHubFollowersUrl

def appendDataToList(gitHubData: list) -> list:
    """Putting the scraped data into a list (in .text format)

    Args:
        gitHubData (list): the raw data

    Returns:
        dataList (list): the processed data
    """
    dataList = []
    for element in gitHubData:
        dataList.append(element.text)
    return dataList


def scrapeFollowers(gitHubFollowersUrl: str) -> list:
    """Scraping all the follower data from a GitHub user.

    Args:
        gitHubFollowersUrl (string): the url of the GitHub user

    Returns:
        list: GitHub followers in a list as dictionaries
    """
    requestContent = requests.get(gitHubFollowersUrl)
    soup = BeautifulSoup(requestContent.content, "html.parser")

    gitHubNames = soup.find_all("span", class_="f4 Link--primary")
    gitHubNamesList = appendDataToList(gitHubNames)

    gitHubUsernames = soup.find_all("span", class_="Link--secondary")
    gitHubUsernamesList = appendDataToList(gitHubUsernames)

    gitHubFollowers = []

    for i in range (len(gitHubNames)):
        gitHubFollower = {
            "name": gitHubNamesList[i],
            "username": gitHubUsernamesList[i]
        }
        gitHubFollowers.append(gitHubFollower)

    return gitHubFollowers


def writeToJson(gitHubFollowerData: list) -> None:
    """Saving the scraped data to JSON to lower undesired traffic to GitHub

    Args:
        gitHubData (list): The follower data in a list
    """
    #GitHub usernames and names go to these lists
    jsonListName, jsonListUsername = [], []

    #Adding the data into two lists
    for dataType in gitHubFollowerData:
        jsonListName.append(dataType["name"])
        jsonListUsername.append(dataType["username"])
    
    #Formulating the content of the JSON file
    jsonContent = {"content": [{"names": jsonListName}, {"usernames": jsonListUsername}]}

    with open(VALUES_INSTANCE.FOLLOWERDATA_FILE_NAME, "w") as jsonFile:
        json.dump(jsonContent, jsonFile)


def scraperProcess() -> None:
    """The main scraping process"""
    gitHubUrl = getUrl()
    gitHubData = scrapeFollowers(gitHubUrl)
    writeToJson(gitHubData)
    print(VALUES_INSTANCE.NOTIFY_SCRAPING_SUCCESSFUL)
