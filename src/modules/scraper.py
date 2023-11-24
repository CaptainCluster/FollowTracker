from bs4 import BeautifulSoup
import requests
import json
import os 
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from variables.values import Values


def getUrl():
    """Retrieving the data from username.txt file

    Returns:
        string: The url in the .txt file
    """
    userNameFile = open("src/username.txt", "r", encoding="utf-8")
    gitHubUrl = userNameFile.readline() 
    gitHubFollowersUrl = gitHubUrl + "?tab=followers" #https://github.com/[the given username]?tab=followers
    return gitHubFollowersUrl


def appendDataToList(gitHubData):
    """Putting the scraped data into a list (in .text format)

    Args:
        gitHubData (list): the raw data

    Returns:
        list: the processed data
    """
    dataList = []
    for element in gitHubData:
        dataList.append(element.text)
    return dataList


def scrapeFollowers(gitHubFollowersUrl):
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


def writeToJson(gitHubFollowerData):
    """Saving the scraped data to JSON to lower undesired traffic to GitHub

    Args:
        gitHubData (list): The follower data in a list
    """

    #GitHub usernames and names go to these lists
    jsonListName = []
    jsonListUsername = []

    jsonFile = open("src/followerdata/followerdata.json", "w")

    #Adding the data into two lists
    for dataType in gitHubFollowerData:
        jsonListName.append(dataType["name"])
        jsonListUsername.append(dataType["username"])
    
    #Formulating the content of the JSON file
    jsonContent = {"content": [{"names": jsonListName}, {"usernames": jsonListUsername}]}
    json.dump(jsonContent, jsonFile)


def scraperProcess():
    """The main scraping process
    """
    values = Values()
    gitHubUrl = getUrl()
    gitHubData = scrapeFollowers(gitHubUrl)
    writeToJson(gitHubData)
    print(values.NOTIFY_SCRAPING_SUCCESSFUL)
