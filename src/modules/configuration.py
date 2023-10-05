import os 
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from variables.values import Values


def askProfileName():
    """If no GitHub user url is identified or username.txt doesn't exist, this
    module is run to define the necessities.
    """
    values = Values()
    gitHubUsername = input(values.ASK_INPUT_USERNAME)
    url = values.URL_START_GITHUB + gitHubUsername #https://github.com/[username]
    
    #Writing the url to the .txt file so that it can be read before scraping
    gitHubUsernameFile = open("src/username.txt", "w", encoding="utf-8")
    gitHubUsernameFile.write(url)

    gitHubUsernameFile.close()
