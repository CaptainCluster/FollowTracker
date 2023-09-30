import modules.configuration as configuration
import modules.scraper as scraper
import modules.analyze as analyze
import modules.write_excel as write_excel
from variables.config import Config
import os

def main():
    #Making sure username.txt exists, in order to get the url to scrape data
    if not os.path.exists("src/username.txt"):
        configuration.askProfileName()

    #If the file exists, we will just make sure its content is valid.
    else:
        config = Config()
        userInputScrape = ""
        urLDefined = False
        usernameFile = open("src/username.txt", "r", encoding="utf-8")
        gitHubUrl = usernameFile.readline()

        gitHubUrlStart = gitHubUrl[:19] #https://github.com/

        if len(gitHubUrl) > 20:
            urLDefined = True
            
        #If something is wrong, we will ask the user for a valid GitHub profile. This writes a new url.
        if gitHubUrlStart != "https://github.com/" or urLDefined == False:
            configuration.askProfileName()
        usernameFile.close()

        #To prevent unnecessary traffic, user needs to confirm they want to scrape data
        while(userInputScrape != "Y" and userInputScrape != "n"):
            userInputScrape = input("Do you want to scrape the follower data?: Y = yes, n = no: ")

            if userInputScrape == "Y":
                scraper.scraperProcess()    
                analyze.compareFollowerLists()
                if config.writingToExcel:
                    write_excel.writeFollowerData()
                break
            elif userInputScrape == "n":
                print("Ending the program!")
                break
            else:
                print("Give a proper input!")

if __name__ == "__main__":
    main()