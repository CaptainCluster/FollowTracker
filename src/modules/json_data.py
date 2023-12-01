import json 
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from variables.values import Values


def getJsonData(jsonDataFileName: str) -> dict:
    """ Fetching data from a selected JSON file

    Args:
        jsonDataFileName (JSON): the JSON file where the data is
    Returns:
        jsonContent (dict): The JSON content from the file
    """
    values = Values()
    try:
        jsonDataFile = open(jsonDataFileName, "r")
        jsonContent = json.load(jsonDataFile)
    except Exception:
        print(values.EXCEPTION_DEFAULT)
    return jsonContent


def handleOldData() -> None:
    """Moving the data from followerdata.json to oldfollowerdata.json
    to stop it from being overwritten, and to make comparisons
    """
    values = Values()
    jsonFile = open("src/followerdata/oldfollowerdata.json", "w")
    #Making sure oldfollowerdata.json exists.
    
    dataToTranfer = getJsonData("src/followerdata/followerdata.json")
    json.dump(dataToTranfer, jsonFile)

