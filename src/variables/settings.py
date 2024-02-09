#------------------------------------------------------#
# Made by CaptainCluster                               #
# https://github.com/captaincluster                    #
#                                                      #
# Settings that allow altering the behavior of the     #
# program.                                             #
#------------------------------------------------------#

class Settings:
    """A class with settings that allow the user to 
    alter the behavior of the program 
    """
    def __init__(self) -> None:
        self.writingToExcel: bool = True
        self.automaticArchival: bool = True 