import json 
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from variables.values import Values


def getJsonData(jsonDataFileName):
    """ Fetching data from a selected JSON file

    Args:
        jsonDataFileName (JSON): the JSON file where the data is
    Returns:
        dict: The JSON content from the file
    """
    values = Values()
    try:
        jsonDataFile = open(jsonDataFileName, "r")
        jsonContent = json.load(jsonDataFile)
    except Exception:
        print(values.EXCEPTION_DEFAULT)
    return jsonContent
