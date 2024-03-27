#------------------------------------------------------#
# Made by CaptainCluster                               #
# https://github.com/captaincluster                    #
#                                                      #
# This tool makes archiving old follower data possible.#
# This prevents the data from being overwritten. By    #
# default, this program works automatically.           #
#------------------------------------------------------#

import os      #Checking if there are available file names
import sys     #To get a precise import for Values class
import shutil  #Copying from one JSON file to another

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from variables.values import Values

VALUES_INSTANCE = Values()

def getFileName() -> None:
    """Fetching the name of an unused "archive" file name with the smallest possible integer at the end

    Args:
        values (Values): a class with pre-defined calues
    """
    try:
        #Looking for a fitting file name for the contents to be archived
        for integer in range(VALUES_INSTANCE.LOOP_LOWER_RANGE, VALUES_INSTANCE.LOOP_HIGHER_RANGE):  
            archiveFileName = VALUES_INSTANCE.ARCHIVE_DIRECTORY + VALUES_INSTANCE.ARCHIVE_FILE_TITLE + str(integer) + VALUES_INSTANCE.ARCHIVE_FILE_FORMAT

            #Writing contents to a file with an unused name
            if not(os.path.exists(archiveFileName)):
                return archiveFileName
            
    except Exception as exception:
        print("Encountered the following error: " + str(exception))

def archiveFollowerData() -> None:
    """Archiving the follower data by copying the data from another JSON file
    """
    archiveFileName = getFileName() #Each archive file has a unique name
    if(archiveFileName != None):
        shutil.copy(VALUES_INSTANCE.OLD_FOLLOWERDATA_FILE_NAME, archiveFileName)
        print(VALUES_INSTANCE.ARCHIVE_SUCCESSFUL + archiveFileName + ".")
    else:
        print(VALUES_INSTANCE.EXCEPTION_ARCHIVE_NULL)

if __name__ == "__main__":
    archiveFollowerData()
