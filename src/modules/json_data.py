#------------------------------------------------------#
# Made by CaptainCluster                               #
# https://github.com/captaincluster                    #
#                                                      #
# This file handles everything related to JSON.        #
#------------------------------------------------------#
import json 
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from variables.values import Values

VALUES_INSTANCE = Values()

def getJsonData(jsonDataFileName: str) -> dict:
    """ Fetching data from a selected JSON file

    Args:
        jsonDataFileName (JSON): the JSON file where the data is
    Returns:
        jsonContent (dict): The JSON content from the file
    """
    try:
        with open(jsonDataFileName, "r") as jsonDataFile:
            jsonContent = json.load(jsonDataFile)
            return jsonContent
    except FileNotFoundError as fnfError:
        print(f"{VALUES_INSTANCE.EXCEPTION_FILE_NOT_FOUND} {str(fnfError)}")
    except Exception as exception:
        print(f"{VALUES_INSTANCE.EXCEPTION_DEFAULT} {str(exception)}")

def handleOldData() -> None:
    """Moving the data from followerdata.json to oldfollowerdata.json
    to stop it from being overwritten, and to make comparisons
    """
    jsonFile = open("followerdata/oldfollowerdata.json", "w")
    dataToTransfer = getJsonData("followerdata/followerdata.json")
    json.dump(dataToTransfer, jsonFile)

