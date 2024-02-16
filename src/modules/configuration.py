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
        print(VALUES_INSTANCE.EXCEPTION_FILE_NOT_FOUND + " " + str(fnfError))
    except Exception as exception:
        print(VALUES_INSTANCE.EXCEPTION_DEFAULT + " " + str(exception))
        
