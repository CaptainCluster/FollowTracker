import modules.configuration as configuration
import modules.scraper as scraper
import modules.analyze as analyze
import modules.write_excel as write_excel
from variables.config import Config
from variables.values import Values
import os

def main():
    """
    The main function of the program
    """
    #Making sure username.txt exists, in order to get the url to scrape data
    values = Values()

    try:
        if not os.path.exists("src/username.txt"):
            configuration.askProfileName()

        #If the file exists, we will just make sure its content is valid.
        else:
            config = Config()
            userInputScrape = ""
            urLDefined = False
            usernameFile = open("src/username.txt", "r", encoding="utf-8")
            gitHubUrl = usernameFile.readline()

            gitHubUrlStart = gitHubUrl[:19] #Meant to be https://github.com/

            if len(gitHubUrl) > 20:
                urLDefined = True
                
            #If something is wrong, we will ask the user for a valid GitHub profile. This writes a new url.
            if gitHubUrlStart != values.URL_START_GITHUB or urLDefined == False:
                configuration.askProfileName()
            usernameFile.close()

            #To prevent unnecessary traffic, user needs to verify that they want to scrape data
            while(userInputScrape != "Y" and userInputScrape != "n"):
                userInputScrape = input(values.REQUEST_SCRAPE)

                if userInputScrape == "Y":

                    #Scraping and analyzing
                    scraper.scraperProcess()    
                    #analyze.compareFollowerLists()

                    #Writing the results to Excel, if it's enabled
                    if config.writingToExcel:
                        write_excel.writeFollowerData()
                    break
                elif userInputScrape == "n":
                    print(values.NOTIFY_ENDING_PROGRAM)
                    break
                else:
                    print(values.NOTIFY_IMPROPER_INPUT)
    except Exception:
        print(values.EXCEPTION_DEFAULT + Exception)

if __name__ == "__main__":
    main()