from openpyxl import Workbook  #Writing the data to an Excel file
import os                      #Finding available file names
import sys                     #A precise import for Values class
import json                    #Fetching the JSON data

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from variables.values import Values


def getFollowerData(values):
    """
    Fetches the follower data from followerdata.json

    Args:
        values (Values): A class full of defined values
    Returns:
        dict: The JSON content from the file
    """
    try:      
        jsonDataFile = open(values.NEW_JSON_FILE, "r")
        jsonContent = json.load(jsonDataFile)
        return jsonContent
    except Exception:
        print(values.EXCEPTION_DEFAULT + Exception)


def excelWriteDefaults(workSheet):
    """
    Adding the default components in the Excel file that won't be changed

    Args:
        workSheet (openpyxl): The worksheet where the changes are appended
    """
    workSheet.cell(row=1, column=1).value = "Usernames" 
    workSheet.cell(row=1, column=2).value = "Names"


def excelChangeColumnWidth(workSheet, widthList):
    """
    Adjusting the lengths of the columns based on the longest data string
    """
    columnList = ["A", "B"]
    for iteration in range(0, (len(columnList)-1)):
        workSheet.column_dimensions[columnList[iteration]].width = widthList[iteration] + 2
        

def excelWritingProcess(values, followerData):
    """
    Writing the data into the Excel file

    Args:
        values (Values): A class full of defined values
        followerData(dict): The data that will be written
    """
    try:
        #Dividing the data into usernames and names
        followerUsernames = followerData["content"][1]["usernames"]
        followerNames = followerData["content"][0]["names"]

        #Setting up the workbook and a worksheet
        wb = Workbook()
        workSheet = wb.worksheets[0]
        workSheet.title = values.EXCEL_WORKSHEET_TITLE

        #Adding the default attributes to the worksheet
        excelWriteDefaults(workSheet)

        widthList = []
        longestLength = 0 #To set width for each column

        longestLength = values.USERNAMES_DEFAULT_WIDTH
        for i, value in enumerate(followerUsernames, start=values.STARTING_ROW):
            workSheet.cell(row=i, column=values.USERNAME_COLUMN).value = value
            if longestLength < len(value):
                longestLength = len(value)
        widthList.append(longestLength)

        longestLength = values.NAMES_DEFAULT_WIDTH
        for i, value in enumerate(followerNames, start=values.STARTING_ROW):

            #If the GitHub follower hasn't defined a name
            if value == "":
                value = "!!UNDEFINED!!"
            workSheet.cell(row=i, column=values.NAME_COLUMN).value = value
            if longestLength < len(value):
                longestLength = len(value)
        widthList.append(longestLength)
        
        excelChangeColumnWidth(workSheet, widthList)

        wb.save(values.EXCEL_FILE)    
    except Exception:
        print(values.EXCEPTION_DEFAULT + Exception)
    

#Main function for writing the data into an Excel file
def writeFollowerData():
    values = Values()
    followerData = getFollowerData(values)
    excelWritingProcess(values, followerData)
    print(values.NOTIFY_WRITING_SUCCESSFUL)

if __name__ == "__main__":
    writeFollowerData()