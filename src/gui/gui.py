#------------------------------------------------------#
# Made by CaptainCluster                               #
# https://github.com/captaincluster                    #
#                                                      #
# This file contains the core class of the GUI         #
# that the program uses.                               #
#------------------------------------------------------#
import tkinter          as tk
from gui.widgets        import Widgets
from variables.values   import Values

VALUES_INSTANCE = Values()

class GUI:
    """The core class of the GUI. A singleton."""
    _instance = None    

    def __new__(cls, root):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.root = root
            cls._instance.root.title(VALUES_INSTANCE.GUI_TITLE)
            cls._instance.root.geometry(VALUES_INSTANCE.GUI_GEOMETRY) 
            cls._instance.widgets = Widgets(cls._instance.root)
            cls._instance.columnRowConfigurations()
            cls._instance.createWidgets()
        return cls._instance
        
    
    def createWidgets(self) -> None:
        """Using a Widgets class object to create the necessary widgets"""
        self.widgets.coreWidgets()
        self.widgets.usernameWidgets()
        self.widgets.notificationWidgets()
    
    def columnRowConfigurations(self) -> None:
        self.root.grid_rowconfigure(3, weight=1) 
        self.root.grid_columnconfigure(0, weight=1) 
        self.root.grid_columnconfigure(1, weight=1) 

    def getInstance(master):
        return GUI(master)

def setUpGUI():
    root = tk.Tk()
    GUI(root)
    root.mainloop()