#------------------------------------------------------#
# Made by CaptainCluster                               #
# https://github.com/captaincluster                    #
#                                                      #
# Setting up the necessities for running the program.  #
# Mostly necessary when used for the first time.       #
#------------------------------------------------------#
import os 
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from variables.values import Values

VALUES_INSTANCE = Values()

def askProfileName() -> None:       #Legacy, to be deleted
    """If no GitHub user url is identified or username.txt doesn't exist, this
    module is run to create the necessities.
    """
    try:
        print(VALUES_INSTANCE.EXCEPTION_NO_URL) #Notifying the user about an undefined url
        gitHubUsername = input(VALUES_INSTANCE.ASK_INPUT_USERNAME)
        url = VALUES_INSTANCE.URL_START_GITHUB + gitHubUsername
        writeUsernameToFile(url)  #Writing the url to a .txt file
    except Exception as exception:
        print(VALUES_INSTANCE.EXCEPTION_DEFAULT + " " + str(exception))

def writeUsernameToFile(url) -> None:
    """A simple function that handles the writing part of the .txt file url assignment
    Args:
        url (string): The url that will be in the .txt file
    """
    try:
        with open(VALUES_INSTANCE.FILE_USERNAME, "w", encoding="utf-8") as gitHubUsernameFile:
            gitHubUsernameFile.write(url)
    except FileNotFoundError as fnfError:
        print(f"{VALUES_INSTANCE.EXCEPTION_FILE_NOT_FOUND} {str(fnfError)}")
    except Exception as exception:
        print(f"{VALUES_INSTANCE.EXCEPTION_DEFAULT} {str(exception)}")

def checkFileExistence() -> None:
    """Making sure that the necessary files exist"""
    try:
        createdFiles = []

        if not(os.path.exists(VALUES_INSTANCE.FILE_USERNAME)):     #Creating an empty file for the GitHub username if it doesn't exist
            with open(VALUES_INSTANCE.FILE_USERNAME, "w", encoding="utf-8") as gitHubUsernameFile:
                createdFiles.append(VALUES_INSTANCE.FILE_USERNAME)
                pass

        #The same process with both of the core JSON files for storing scraped follower data
        if not(os.path.exists(VALUES_INSTANCE.NEW_JSON_FILE)):
            with open(VALUES_INSTANCE.NEW_JSON_FILE, "w", encoding="utf-8") as followerDataJsonFile:
                createdFiles.append(VALUES_INSTANCE.NEW_JSON_FILE)
                pass
        if not(os.path.exists(VALUES_INSTANCE.OLD_JSON_FILE)):
            with open(VALUES_INSTANCE.OLD_JSON_FILE, "w", encoding="utf-8") as oldFollowerDataJsonFile:
                createdFiles.append(VALUES_INSTANCE.OLD_JSON_FILE)
                pass
        #Printing to the terminal, only if files have been created
        if(len(createdFiles) > 0):
            print(VALUES_INSTANCE.NOTIFY_LISTING_CREATED_FILES)
            for createdFile in createdFiles:
                if createdFile == createdFiles[len(createdFiles)-1]: #No comma behind the last entry
                    print(createdFile)
                    pass
                print(createdFile, end= ", ")
    except Exception as exception:
        print(VALUES_INSTANCE.EXCEPTION_DEFAULT + str(exception))
