import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import tkinter          as tk
from variables.values   import Values
from gui.gui            import GUI

VALUES_INSTANCE = Values()

def setUpGUI() -> None:
    """Graphical User Interface, allowing the user to interact with the program"""
    root = tk.Tk()
    my_gui = GUI(root)
    root.mainloop()

def main() -> None:
    """The core function of the program"""
    try:
        setUpGUI()
        
    except Exception as exception:
        #If GUI can't be established, the error must be printed out
        print(VALUES_INSTANCE.EXCEPTION_DEFAULT + str(exception))

if __name__ == "__main__":
    main()