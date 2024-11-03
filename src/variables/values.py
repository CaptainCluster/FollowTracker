#------------------------------------------------------#
# Made by CaptainCluster                               #
# https://github.com/captaincluster                    #
#                                                      #
# A bunch of constants arranged into one place.        #
#------------------------------------------------------#
class Values:
    def __init__(self) -> None:
        """
        Multiple essential values used in this program are stored here to allow
        flexibility and easy management.
        """
       
        self.LOOP_LOWER_RANGE: int  = 1
        self.LOOP_HIGHER_RANGE: int = 100

         #-------- Notifications --------#
        self.NOTIFY_SCRAPE_START                = "Scraping data..."
        self.NOTIFY_ENDING_PROGRAM              = "Ending the program!"
        self.NOTIFY_IMPROPER_INPUT              = "Give a proper input!"
        self.NOTIFY_SCRAPING_SUCCESSFUL         = "Data has been successfully scraped."
        self.NOTIFY_WRITING_SUCCESSFUL          = "The data has been successfully written into an Excel file."
        self.NOTIFY_SUBMIT_USERNAME_SUCCESSFUL  = "GitHub username submitted successfully."


        self.ARCHIVE_SUCCESSFUL         = "The data has been archived successfully to " # + file name

        #-------- Exceptions --------#
        self.EXCEPTION_NO_URL                   = "A GitHub username has not been selected."
        self.EXCEPTION_DEFAULT                  = "An error has occurred:"
        self.EXCEPTION_ARCHIVE_NULL             = "No suitable archive file name found."
        self.EXCEPTION_FILE_NOT_FOUND           = "Unable to find the file."
        self.EXCEPTION_USERNAME_FILE_NOT_FOUND  = "No username identified. Make sure you submit your GitHub username first."
        self.EXCEPTION_EMPTY_SUBMISSION         = "You need to insert your GitHub username in order to submit it."
        self.EXCEPTION_SCRAPE_FAIL              = "Failed to retrieve followers: "
        #-------- Files & Directories --------#


        self.ARCHIVE_FILE_FORMAT    = ".json"
        self.ARCHIVE_FILE_TITLE     = "archive"
        self.ARCHIVE_DIRECTORY      = "src/followerData/archive/"

        self.FOLLOWERDATA_FILE_NAME     = "followerdata/followerdata.json"
        self.OLD_FOLLOWERDATA_FILE_NAME = "followerdata/oldfollowerdata.json"

        self.FILE_USERNAME = "username.txt"    

        #-------- Configurations --------#
        self.NOTIFY_LISTING_CREATED_FILES = "The following required files have been created: "

        #-------- Excel Configurations --------#
        self.EXCEL_FILE             = "followerdata/excel/followerdata.xlsx"
        self.EXCEL_WORKSHEET_TITLE  = "FollowTracker"

        self.EXCEL_UNDEFINED_VALUE  = "!UNDEFINED!"  #If a GitHub user has no name, an exception will clarify that

        self.USERNAME_COLUMN    = 1
        self.STARTING_ROW       = 2   #The first row for data insertion

        self.USERNAMES_DEFAULT_WIDTH    = len("usernames")
        self.NAMES_DEFAULT_WIDTH        = len("names")

        #-------- Misc --------#
        self.REQUEST_SCRAPE     = "Do you want to scrape the follower data?: Y = yes, n = no: "

        #-------- GUI --------#
        self.GUI_TITLE          = "FollowTracker"
        self.GUI_GEOMETRY       = "375x225"
        self.GUI_LABEL_DEFAULT  = "Notifications Come Here"
        
        self.ASK_INPUT_USERNAME = "What is your username: "

        

        
        
