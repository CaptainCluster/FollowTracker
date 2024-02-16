import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from variables.values   import Values
from gui.gui            import setUpGUI

VALUES_INSTANCE = Values()

def main() -> None:
    """The core function of the program"""
    try:
        setUpGUI()
        
    except Exception as exception:
        #If GUI can't be established, the error must be printed out
        print(VALUES_INSTANCE.EXCEPTION_DEFAULT + str(exception))

if __name__ == "__main__":
    main()