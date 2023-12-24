class Values:
    def __init__(self) -> None:
        """
        Multiple essential values used in this program are stored here to allow
        flexibility and easy management.
        """

        ### Notifications ###
        self.LOOP_LOWER_RANGE: int = 1
        self.LOOP_HIGHER_RANGE: int = 100

        self.NOTIFY_SCRAPE_START = "Scraping data..."
        self.NOTIFY_ENDING_PROGRAM = "Ending the program!"
        self.NOTIFY_IMPROPER_INPUT = "Give a proper input!"
        self.NOTIFY_SCRAPING_SUCCESSFUL = "Data has been successfully scraped."
        self.NOTIFY_WRITING_SUCCESSFUL = "The data has been successfully written into an Excel file."

        self.ARCHIVE_SUCCESSFUL = "The data has been archived successfully to " # + file name
        #####################


        ### Exceptions ###
        self.EXCEPTION_NO_URL = "A GitHub username has not been selected."
        self.EXCEPTION_DEFAULT = "An error has occurred."
        self.EXCEPTION_ARCHIVE_NULL = "No suitable archive file name found."
        ##################


        ### User Inputs ###
        self.USER_YES_INPUT = "Y"
        self.USER_NO_INPUT = "n"
        self.ASK_INPUT_USERNAME = "Type your GitHub username over here: "
        ###################


        ### Files & Directories ###
        self.FILE_USERNAME = "src/username.txt"

        self.NEW_JSON_FILE = "src/followerdata/followerdata.json"       #Fresh follower data
        self.OLD_JSON_FILE = "src/followerdata/oldfollowerdata.json"    #Where the formerly fresh data is placed

        self.ARCHIVE_FILE_FORMAT = ".json"
        self.ARCHIVE_FILE_TITLE = "archive"
        self.ARCHIVE_DIRECTORY = "src/followerData/archive/"

        self.FOLLOWERDATA_FILE_NAME = "src/followerdata/followerdata.json"
        self.OLD_FOLLOWERDATA_FILE_NAME = "src/followerdata/oldfollowerdata.json"

        self.FILE_USERNAME = "src/username.txt"
        ############################
    

        ### Excel Configurations ###
        self.EXCEL_FILE = "src/followerdata/excel/followerdata.xlsx"
        self.EXCEL_WORKSHEET_TITLE = "FollowTracker"

        self.EXCEL_UNDEFINED_VALUE = "!UNDEFINED!"  #If a GitHub user has no name, an exception will clarify that

        self.USERNAME_COLUMN = 1
        self.NAME_COLUMN = 2
        self.STARTING_ROW = 2   #The first row for data insertion

        self.USERNAMES_DEFAULT_WIDTH = len("usernames")
        self.NAMES_DEFAULT_WIDTH = len("names")
        ############################


        ########### Misc ###########
        self.REQUEST_SCRAPE = "Do you want to scrape the follower data?: Y = yes, n = no: "
        self.URL_START_GITHUB = "https://github.com/"
        ############################
    


        

        
        