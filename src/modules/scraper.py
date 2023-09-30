from bs4 import BeautifulSoup
import requests
import json

#Retrieving the url from username.txt file
def getUrl():
    userNameFile = open("src/username.txt", "r", encoding="utf-8")
    gitHubUrl = userNameFile.readline() 
    gitHubFollowersUrl = gitHubUrl + "?tab=followers" #https://github.com/[the given username]?tab=followers
    return gitHubFollowersUrl

#Putting scraped data into a list
def appendDataToList(gitHubData):
    dataList = []
    for element in gitHubData:
        dataList.append(element.text)
    return dataList

#Scraping all the follower data from a GitHub user.
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

#Saving the scraped data to JSON to lower undesired traffic to GitHub
def writeToJson(gitHubData):
    jsonListName = []
    jsonListUsername = []
    jsonFile = open("src/followerdata/followerdata.json", "w")
    for dataType in gitHubData:
        jsonListName.append(dataType["name"])
        jsonListUsername.append(dataType["username"])

    jsonContent = {"content": [{"names": jsonListName}, {"usernames": jsonListUsername}]}
    json.dump(jsonContent, jsonFile)


#def compareData():
#    return None

#The main scraping process
def scraperProcess():
    gitHubUrl = getUrl()
    gitHubData = scrapeFollowers(gitHubUrl)
    writeToJson(gitHubData)
    print("Data has been successfully scraped.")
