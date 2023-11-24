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
    workSheet.cell(row=1, column=1).value   = "Usernames" 
    workSheet.cell(row=1, column=2).value   = "Names"
    workSheet.cell(row=1, column=3).value   = "Links"

    workSheet.cell(row=1, column=6).value   = "Total Followers"
    workSheet.cell(row=4, column=6).value   = "Total Followed"
    workSheet.cell(row=7, column=6).value   = "Total Unfollowed"

    workSheet.cell(row=10, column=6).value  = "Net Change"

    workSheet.cell(row=1, column=4).value   = "New Followers"
    workSheet.cell(row=1, column=5).value   = "New Unfollowers"


def excelChangeColumnWidth(workSheet, widthList) -> None:
    """
    Adjusting the lengths of the columns based on the longest data string
    """
    columnList = ["A", "B", "C", "D"]   #To identify the columns
    for iteration in range(0, (len(columnList)-1)):
        workSheet.column_dimensions[columnList[iteration]].width = widthList[iteration] + 2
        

def setUpExcel(values) -> Workbook:
    """ Setting up the workbook and the worksheet

    Args:
        values (Values): A class full of pre-defined values

    Returns:
        wb: the Excel workbook
        worksheet: the Excel worksheet
    """
    wb = Workbook()
    workSheet = wb.worksheets[0]
    workSheet.title = values.EXCEL_WORKSHEET_TITLE

    return wb, workSheet


def excelWritingProcess(values, followerData) -> None:
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

        #Getting the data for fresh followers and those who unfollowed
        changedFollowershipList = analyze.compareFollowerLists()
        followedList, unfollowedList = changedFollowershipList 


        #Setting up the workbook and a worksheet
        wb, workSheet = setUpExcel(values)

        #Adding the default attributes to the worksheet
        excelWriteDefaults(workSheet)

        widthList = []

        widthList.append(writeListToExcel(workSheet, values, followerUsernames, values.USERNAME_COLUMN, None))
        widthList.append(writeListToExcel(workSheet, values, followerNames, values.NAME_COLUMN, None))
        widthList.append(writeListToExcel(workSheet, values, followerUsernames, 3, values.URL_START_GITHUB))
        widthList.append(writeListToExcel(workSheet, values, followedList, 4, None))
        widthList.append(writeListToExcel(workSheet, values, unfollowedList, 5, None))

        workSheet.cell(row=2, column=6).value = len(followerUsernames)
        workSheet.cell(row=5, column=6).value = len(followedList)
        workSheet.cell(row=8, column=6).value = len(unfollowedList)
        workSheet.cell(row=11, column=6).value = (len(followedList)-len(unfollowedList))

        excelChangeColumnWidth(workSheet, widthList)

        wb.save(values.EXCEL_FILE)    
    except Exception as exception:
        print(values.EXCEPTION_DEFAULT + str(exception))
    

def writeListToExcel(workSheet, values, dataList, writeColumn, dataString) -> int:
    """Writing a list, using a for-loop, to an Excel file

    Args:
        workSheet (openpyxl): The worksheet where the changes are appended
        values (Values): A class full of defined values
        dataList (list): All the data to be written
        writeColumn (int): The column in the Excel file where the data is written
        dataString (string/None): A potential string in front of the given data

    Returns:
        longestLength (int): Integer for determining column width
    """
    longestLength = values.USERNAMES_DEFAULT_WIDTH
    
    for i, value in enumerate(dataList, start=values.STARTING_ROW):

        #Handling undefined values
        if value == "":
                value = values.EXCEL_UNDEFINED_VALUE
        
        #A potential string in front of the written data
        if dataString:
            value = dataString + value

        #The longest length allows us to determine a proper width for a column in Excel
        if len(value) > longestLength:
            longestLength = len(value)

        workSheet.cell(row=i, column=writeColumn).value = value
    
    return longestLength
        

def writeFollowerData() -> None:
    """The core function for writing the data into an Excel file
    """
    values = Values()
    followerData = json_data.getJsonData(values.FOLLOWERDATA_FILE_NAME)
    excelWritingProcess(values, followerData)
    print(values.NOTIFY_WRITING_SUCCESSFUL)


if __name__ == "__main__":
    writeFollowerData()