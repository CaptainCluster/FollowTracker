from openpyxl import Workbook  #Writing the data to an Excel file
import os                      #Finding available file names
import sys                     #A precise import for Values class

sys.path.insert(1, os.path.join(sys.path[0], '..'))
import modules.json_data as json_data
import modules.analyze as analyze

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from variables.values import Values


def excelWriteDefaults(workSheet):
    """
    Adding the default components in the Excel file that won't be changed

    Args:
        workSheet (openpyxl): The worksheet where the changes are appended
    """
    workSheet.cell(row=1, column=1).value = "Usernames" 
    workSheet.cell(row=1, column=2).value = "Names"
    workSheet.cell(row=1, column=3).value = "Links"
    workSheet.cell(row=1, column=4).value = "Total Followers"
    workSheet.cell(row=4, column=4).value = "Total Followed"
    workSheet.cell(row=7, column=4).value = "Total Unfollowed"
    workSheet.cell(row=10, column=4).value = "Net Change"


def excelChangeColumnWidth(workSheet, widthList):
    """
    Adjusting the lengths of the columns based on the longest data string
    """
    columnList = ["A", "B", "C", "D"]
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

        changedFollowershipList = analyze.compareFollowerLists()
        followedList = changedFollowershipList[0]
        unfollowedList = changedFollowershipList[1]


        #Setting up the workbook and a worksheet
        wb = Workbook()
        workSheet = wb.worksheets[0]
        workSheet.title = values.EXCEL_WORKSHEET_TITLE

        #Adding the default attributes to the worksheet
        excelWriteDefaults(workSheet)

        widthList = []
        longestLength = 0 #To set width for each column
        linkLongestLength = 0

        longestLength = values.USERNAMES_DEFAULT_WIDTH
        for i, value in enumerate(followerUsernames, start=values.STARTING_ROW):
            workSheet.cell(row=i, column=values.USERNAME_COLUMN).value = value
            if longestLength < len(value):
                longestLength = len(value)
            #Adding the link as well
            gitHubUserLink = "https://github.com/" + value
            workSheet.cell(row=i, column = 3).value = gitHubUserLink
            if linkLongestLength < len(gitHubUserLink):
                linkLongestLength = len(gitHubUserLink)
        
        widthList.append(longestLength)
        widthList.append(linkLongestLength)

        longestLength = values.NAMES_DEFAULT_WIDTH
        for i, value in enumerate(followerNames, start=values.STARTING_ROW):

            #If the GitHub follower hasn't defined a name
            if value == "":
                value = "!!UNDEFINED!!"
            workSheet.cell(row=i, column=values.NAME_COLUMN).value = value
            if longestLength < len(value):
                longestLength = len(value)
        widthList.append(longestLength)

        workSheet.cell(row=2, column=4).value = len(followerUsernames)
        workSheet.cell(row=5, column=4).value = len(followedList)
        workSheet.cell(row=8, column=4).value = len(unfollowedList)
        workSheet.cell(row=11, column=4).value = (len(followedList)-len(unfollowedList))
        
        excelChangeColumnWidth(workSheet, widthList)

        wb.save(values.EXCEL_FILE)    
    except Exception:
        print(values.EXCEPTION_DEFAULT + Exception)
    

#Main function for writing the data into an Excel file
def writeFollowerData():
    values = Values()
    followerData = json_data.getJsonData(values.FOLLOWERDATA_FILE_NAME)
    excelWritingProcess(values, followerData)
    print(values.NOTIFY_WRITING_SUCCESSFUL)

if __name__ == "__main__":
    writeFollowerData()