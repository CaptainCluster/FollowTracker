class Values:
    def __init__(self):
        """A class consisting of multiple defined values in a way
        that allows them to be maintained easily
        """
        self.EXCEPTION_DEFAULT = "Encountered an error."

        self.LOOP_LOWER_RANGE = 1
        self.LOOP_HIGHER_RANGE = 100

        self.NOTIFY_SCRAPING_SUCCESSFUL = "Data has been successfully scraped."

        ## main.py ##
        self.USER_YES_INPUT = "Y"
        self.USER_NO_INPUT = "n"
        self.NOTIFY_SCRAPE_START = "Scraping data..."
        self.NOTIFY_ENDING_PROGRAM = "Ending the program!"
        self.NOTIFY_IMPROPER_INPUT = "Give a proper input!"
        self.REQUEST_SCRAPE = "Do you want to scrape the follower data?: Y = yes, n = no: "

        ## configuration.py ##
        self.ASK_INPUT_USERNAME = "Type your GitHub username over here: "
        self.URL_START_GITHUB = "https://github.com/"

        ## analyze.py ##
        self.NEW_JSON_FILE = "src/followerdata/followerdata.json"
        self.OLD_JSON_FILE = "src/followerdata/oldfollowerdata.json" 

        ## archiver.py ##
        self.ARCHIVE_FILE_FORMAT = ".json"
        self.ARCHIVE_FILE_TITLE = "archive"
        self.ARCHIVE_DIRECTORY = "src/followerData/archive/"

        self.FOLLOWERDATA_FILE_NAME = "src/followerdata/followerdata.json"
        self.OLD_FOLLOWERDATA_FILE_NAME = "src/followerdata/oldfollowerdata.json"

        self.EXCEPTION_ARCHIVE_NULL = "No suitable archive file name found."
        self.ARCHIVE_SUCCESSFUL = "The data has been archived successfully to " # + file name

        ## write_excel.py ##
        self.EXCEL_FILE = "src/followerdata/excel/followerdata.xlsx"
        self.EXCEL_WORKSHEET_TITLE = "FollowTracker"

        self.USERNAME_COLUMN = 1
        self.NAME_COLUMN = 2
        self.STARTING_ROW = 2 #The first row for data insertion

        self.USERNAMES_DEFAULT_WIDTH = len("usernames")
        self.NAMES_DEFAULT_WIDTH = len("names")

        self.NOTIFY_WRITING_SUCCESSFUL = "The data has been successfully written into an Excel file."
        
        
