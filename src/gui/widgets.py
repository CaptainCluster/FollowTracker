#------------------------------------------------------#
# Made by CaptainCluster                               #
# https://github.com/captaincluster                    #
#                                                      #
# This file contains the cwidgets that the GUI         #
# utilizes.                                            #
#------------------------------------------------------#
from   tkinter import ttk 
from   tkinter import * 

import os 
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from modules.configuration  import writeUsernameToFile
import modules.scraper      as Scraper
import modules.write_excel  as WriteExcel
from variables.values       import Values
from variables.settings     import Settings
import tools.archiver       as Archiver


VALUES_INSTANCE = Values()
SETTINGS_INSTANCE = Settings()

class Widgets:
    """Handles all the widgets utilized by the GUI"""
    def __init__(self, root) -> None:
        self.root = root

    def coreWidgets(self) -> None:
        self.scrapeButton = ttk.Button(self.root, text="Scrape Content", command=self.scrapeContent)
        self.scrapeButton.grid(row=2, column=0, columnspan=2, pady=(20, 10), padx=20, sticky='ew')

    def usernameWidgets(self) -> None:
        """Widgets that are responsible of saving the GitHub account url"""
        self.usernameLabel = ttk.Label(self.root, text="GitHub Username:")
        self.usernameLabel.grid(row=0, column=0, padx=20, pady=(20, 5), sticky='w')

        self.usernameEntry = ttk.Entry(self.root)
        self.usernameEntry.grid(row=0, column=1, padx=20, pady=(20, 5), sticky='ew')

        self.submitUsernameButton = ttk.Button(self.root, text="Submit", command=self.writeGitHubUrlToFile)
        self.submitUsernameButton.grid(row=1, column=0, columnspan=2, pady=5, padx=20, sticky='ew')

    def notificationWidgets(self) -> None:
        self.notificationLabel = ttk.Label(self.root, text="Notifications will appear here.", wraplength=400)
        self.notificationLabel.grid(row=3, column=0, columnspan=2, pady=(10, 20), padx=20, sticky='ew')

    def writeGitHubUrlToFile(self) -> None:
        try:
            githubUsername = self.usernameEntry.get()

            if(githubUsername == ""):
                self.createNotification("You need to insert your GitHub username in order to submit it.")
                return

            githubUrl = "https://github.com/" + githubUsername
            writeUsernameToFile(githubUrl)
            self.usernameEntry.delete(0, "end")
            self.createNotification("GitHub username submitted successfully.")

        except Exception as exception:
            self.createNotification(VALUES_INSTANCE.EXCEPTION_DEFAULT + str(exception))

    def scrapeContent(self) -> None:
        try:
            Scraper.scraperProcess()
            if SETTINGS_INSTANCE.writingToExcel:
                WriteExcel.writeFollowerData()
            if SETTINGS_INSTANCE.automaticArchival:
                Archiver.archiveFollowerData()
            self.createNotification("Scraping process completed successfully!")

        except IOError:
            self.createNotification(VALUES_INSTANCE.EXCEPTION_USERNAME_FILE_NOT_FOUND)
        
        except Exception as exception:
            self.createNotification(VALUES_INSTANCE.EXCEPTION_DEFAULT + str(exception))

    def createNotification(self, notification) -> None:
        """Displaying a message for the user in the GUI.

        Args:
            notification (str): The string displayed to the user
        """
        try:    
            self.notificationLabel.config(text=notification)
            self.notificationLabel.config(wraplength=300) 
   
        except Exception as exception:
            self.notificationLabel.config(text=VALUES_INSTANCE.EXCEPTION_DEFAULT + str(exception))
