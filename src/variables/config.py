class Config:
    """A class with settings that allow the user to 
    alter the behavior of the program 
    """
    def __init__(self) -> None:
        self.writingToExcel: bool = True
        self.automaticArchival: bool = True 