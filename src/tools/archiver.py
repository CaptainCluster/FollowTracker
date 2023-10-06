#Drive this program to archive your follower data so it won't be overwritten.

import os      #Checking if there are available file names
import sys     #To get a precise import for Values class
import shutil  #Copying from one JSON file to another

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from variables.values import Values

#Fetching the name of an unused file name with the smallest possible integer
def getFileName(values):
    try:
        #Looking for a fitting file name for the contents to be archived
        for integer in range(values.LOOP_LOWER_RANGE, values.LOOP_HIGHER_RANGE):  
            archiveFileName = values.ARCHIVE_DIRECTORY + values.ARCHIVE_FILE_TITLE + str(integer) + values.ARCHIVE_FILE_FORMAT

            #Writing contents to a file with an unused name
            if not(os.path.exists(archiveFileName)):
                return archiveFileName
    except Exception:
        print("Encountered the following error: " + Exception)

def archiveFollowerData():
    values = Values()
    archiveFileName = getFileName(values)

    if(archiveFileName != None):
        shutil.copy(values.OLD_FOLLOWERDATA_FILE_NAME, archiveFileName)
        print(values.ARCHIVE_SUCCESSFUL + archiveFileName + ".")
    else:
        print(values.EXCEPTION_ARCHIVE_NULL)

if __name__ == "__main__":
    archiveFollowerData()
