from openpyxl import Workbook  #Writing the data to an Excel file
import os                      #Finding available file names
import sys                     #A precise import for Values class
import json                    #Fetching the JSON data

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from variables.values import Values

#Getting the follower data from followerdata.json
def getData(values):
    try:      
        jsonDataFileName = "src/followerdata/followerdata.json"
        jsonDataFile = open(jsonDataFileName, "r")
        jsonContent = json.load(jsonDataFile)
        return jsonContent
    except Exception:
        print(values.EXCEPTION_DEFAULT + Exception)

#Writing the content that will be the same no matter what
def excelWriteDefault(workSheet):
    workSheet.cell(row=1, column=1).value = "Usernames" 
    workSheet.cell(row=1, column=2).value = "Names"

#Adjusting the lengths of the columns based on the longest data string
def excelChangeColumnWidth(workSheet, widthList):
    columnList = ["A", "B"]
    iteration = 0
    while iteration < len(columnList):
        workSheet.column_dimensions[columnList[iteration]].width = widthList[iteration] + 2
        iteration += 1
        
def excelWritingProcess(values, followerData):
    try:
        followerUsernames = followerData["content"][1]["usernames"]
        followerNames = followerData["content"][0]["names"]

        wb = Workbook()
        workSheet = wb.worksheets[0]
        workSheet.title = "FollowTracker"

        excelWriteDefault(workSheet)

        widthList = []
        longestLength = 0 #To set width for each column

        longestLength = len("Usernames")
        for i, value in enumerate(followerUsernames, start=values.STARTING_ROW):
            workSheet.cell(row=i, column=values.USERNAME_COLUMN).value = value
            if longestLength < len(value):
                longestLength = len(value)
        widthList.append(longestLength)

        longestLength = len("Names")
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
    followerData = getData(values)
    excelWritingProcess(values, followerData)
    print(values.NOTIFY_WRITING_SUCCESSFUL)

if __name__ == "__main__":
    writeFollowerData()