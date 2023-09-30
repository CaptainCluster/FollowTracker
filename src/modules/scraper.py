from bs4 import BeautifulSoup
import requests
import json
import sys

#The GitHub followers of a profile are in a slightly different url.
#We will add "?tab=followers" into the url we already have.
def getUrl():
    userNameFile = open("src/username.txt", "r", encoding="utf-8")
    gitHubUrl = userNameFile.readline()
    #The url: https://github.com/[the given username]?tab=followers
    gitHubFollowersUrl = gitHubUrl + "?tab=followers"
    return gitHubFollowersUrl

def appendDataToList(gitHubData):
    dataList = []
    for element in gitHubData:
        dataList.append(element.text)
    return dataList

#Here we will scrape all the data from GitHub.
def scrapeFollowers(gitHubFollowersUrl):
    requestContent = requests.get(gitHubFollowersUrl)
    soup = BeautifulSoup(requestContent.content, "html.parser")

    gitHubNames = soup.find_all("span", class_="f4 Link--primary")
    gitHubNamesList = appendDataToList(gitHubNames)

    gitHubUsernames = soup.find_all("span", class_="Link--secondary pl-1")
    gitHubUsernamesList = appendDataToList(gitHubUsernames)
    
    gitHubFollowers = []
    for i in range (len(gitHubNames) - 3):
        gitHubFollower = {
            "name": gitHubNamesList[i],
            "username": gitHubUsernamesList[i]
        }
        gitHubFollowers.append(gitHubFollower)
    return gitHubFollowers

#To reduce traffic to GitHub and make comparisons easier, we will save 
#the scraped data into a JSON file.
def writeToJson(gitHubData):
    jsonListName = []
    jsonListUsername = []
    jsonFile = open("src/followerdata/followerdata.json", "w")
    for dataType in gitHubData:
        jsonListName.append(dataType["name"])
        jsonListUsername.append(dataType["username"])

    jsonContent = {"content": [{"names": jsonListName}, {"usernames": jsonListUsername}]}
    json.dump(jsonContent, jsonFile)

#Comparing the old follower list to the new one to figure out if someone
#has followed or unfollowed the profile of your url.
def compareData():
    return None

def scraperProcess():
    gitHubUrl = getUrl()
    gitHubData = scrapeFollowers(gitHubUrl)
    writeToJson(gitHubData)
    print("Data has been successfully scraped.")
