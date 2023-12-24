import modules.configuration as configuration
import modules.scraper as scraper
import modules.write_excel as write_excel
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from variables.config import Config
from variables.values import Values
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import modules.json_data as json_data
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import tools.archiver as archiver

def main() -> None:
    """The main function of the program"""

    #Making sure username.txt exists, in order to get the url to scrape data
    values = Values()

    try:
        if not os.path.exists(values.FILE_USERNAME):
            configuration.askProfileName()

        #If the file exists, we will just make sure its content is valid.
        config = Config()
        userInputScrape = ""
        urLDefined = False
        usernameFile = open(values.FILE_USERNAME, "r", encoding="utf-8")
        gitHubUrl = usernameFile.readline()

        gitHubUrlStart = gitHubUrl[:19] #Meant to be https://github.com/

        if len(gitHubUrl) > 20:
            urLDefined = True
            
        #If something is wrong, we will ask the user for a valid GitHub profile. This writes a new url.
        if gitHubUrlStart != values.URL_START_GITHUB or urLDefined == False:
            configuration.askProfileName()
        usernameFile.close()

        #To prevent unnecessary traffic, user needs to verify that they want to scrape data
        while(userInputScrape != values.USER_YES_INPUT and userInputScrape != values.USER_NO_INPUT):
            userInputScrape = input(values.REQUEST_SCRAPE)

            if userInputScrape == values.USER_YES_INPUT:
                print(values.NOTIFY_SCRAPE_START)

                #Scraping and analyzing
                scraper.scraperProcess()    

                #Writing the results to Excel, if it's enabled
                if config.writingToExcel:
                    write_excel.writeFollowerData()
                
                #Moving the older data from followerdata.json to oldfollowerdata.json
                json_data.handleOldData()

                #If automatic archival is enabled, the older data will be archived
                if config.automaticArchival:
                    archiver.archiveFollowerData()
                break
            elif userInputScrape == values.USER_NO_INPUT:
                print(values.NOTIFY_ENDING_PROGRAM)
                break
            else:
                print(values.NOTIFY_IMPROPER_INPUT)
    except Exception as exeption:
        print(values.EXCEPTION_DEFAULT + print(Exception))

if __name__ == "__main__":
    main()