#TODO: create a class called DataExtractor to extract key information from the given news


class DataExtractor:
    def __init__(self, news:str):
        """
			Constructor for the Data extractor class
			Initializes the object
        """
        self.news = news
        
    def getLocation(self) -> str:
        """
			Returns the location where the accident had happened
        """
        raise NotImplementedError
    
    def getDate(self):
        """
			Returns the date of the accident
        """
        raise NotImplementedError
    
    def getDeathNumber(self):
        raise NotImplementedError
    
    def getInjuryNumber(self):
        raise NotImplementedError
    