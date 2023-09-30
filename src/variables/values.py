class Values:
    def __init__(self):
        self.EXCEPTION_DEFAULT = "Encountered the following error: "

        self.LOOP_LOWER_RANGE = 1
        self.LOOP_HIGHER_RANGE = 100

        ## analyze.py ##
        self.NEW_JSON_FILE = "src/followerdata/followerdata.json"
        self.OLD_JSON_FILE = "src/followerdata/oldfollowerdata.json" 

        ## archiver.py ##
        self.ARCHIVE_FILE_FORMAT = ".json"
        self.ARCHIVE_FILE_TITLE = "archive"
        self.ARCHIVE_DIRECTORY = "src/followerData/archive/"

        self.FOLLOWERDATA_FILE_NAME = "src/followerdata/followerdata.json"

        self.EXCEPTION_ARCHIVE_NULL = "No suitable archive file name found."
        self.ARCHIVE_SUCCESSFUL = "The data has been archived successfully to " # + file name

        ## write_excel.py ##
        self.EXCEL_FILE = "src/followerdata/excel/followerdata.xlsx"

        self.USERNAME_COLUMN = 1
        self.NAME_COLUMN = 2
        self.STARTING_ROW = 2 #The first row for data insertion

        self.NOTIFY_WRITING_SUCCESSFUL = "The data has been successfully written into an Excel file."
        
