import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from modules.configuration  import checkFileExistence
from variables.values       import Values
from gui.gui                import setUpGUI

VALUES_INSTANCE = Values()

def main() -> None:
    """The core function of the program.

    Here is how the program works:
        1. Making sure the necessary files exist in order to 
        help assure a satisfactory performance and outcome.

        2. Setting up a GUI that allows the use of the program.
    """
    try:
        checkFileExistence()
        setUpGUI()
        
    except Exception as exception:
        #If a GUI can't be established, the error must be printed out
        print(VALUES_INSTANCE.EXCEPTION_DEFAULT + str(exception))

if __name__ == "__main__":
    main()