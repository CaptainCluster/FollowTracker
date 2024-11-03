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


def scrapeFollowers() -> list:
    """Scraping all the follower data from a GitHub user.

    Args:
        gitHubFollowersUrl (string): the url of the GitHub user

    Returns:
        list: GitHub followers in a list as dictionaries
    """

    perPage = 100
    page = 1
    followerList = []
    gitHubFollowers = []
    usernameFile = open(VALUES_INSTANCE.FILE_USERNAME, "r", encoding="utf-8")
    username = usernameFile.readline()
    usernameFile.close()

    while True:
        gitHubUrl = f"https://api.github.com/users/{username}/followers?per_page={perPage}&page={page}"
        print(gitHubUrl)
        response = requests.get(gitHubUrl) 
    
        # Handling a failed scrape 
        if not response.status_code == 200:
            print(f"{VALUES_INSTANCE.EXCEPTION_SCRAPE_FAIL} {response.status_code}")
            break

        # A successful scrape 
        followerData = response.json()
        
        # If the follower data is empty
        if not followerData:
            break

        followerList.extend(followerData)
        page += 1
    
    if len(followerList) == 0:
        return gitHubFollowers

    for follower in followerList:
        gitHubFollowerEntry = {
            "username": str(follower["login"]),
            "url": follower["html_url"]
        }
        gitHubFollowers.append(gitHubFollowerEntry)

    return gitHubFollowers


def writeToJson(gitHubFollowerData: list) -> None:
    """Saving the scraped data to JSON to lower undesired traffic to GitHub

    Args:
        gitHubData (list): The follower data in a list
    """
    #GitHub usernames and names go to these lists
    jsonListUsername, jsonListUrl = [], []

    #Adding the data into two lists
    for dataType in gitHubFollowerData:
        jsonListUsername.append(dataType["username"])
        jsonListUrl.append(dataType["url"])
    
    #Formulating the content of the JSON file
    jsonContent = {"content": [{"usernames": jsonListUsername, "urls": jsonListUrl}]}

    with open(VALUES_INSTANCE.FOLLOWERDATA_FILE_NAME, "w") as jsonFile:
        json.dump(jsonContent, jsonFile)


def scraperProcess() -> None:
    """The main scraping process"""
    gitHubData = scrapeFollowers()
    writeToJson(gitHubData)
    print(VALUES_INSTANCE.NOTIFY_SCRAPING_SUCCESSFUL)
