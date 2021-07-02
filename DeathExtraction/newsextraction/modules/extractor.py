#TODO: create a class called DataExtractor to extract key information from the given news
from .tagger import Tagger
from .tokenizer import Tagger


class DataExtractor:
	def __init__(self, posTaggedSentences, newsStory: str):
		"""
			Constructor for the Data extractor class
			Initializes the object
		"""
		self.news = newsStory
		self.posTaggedSentences = posTaggedSentences

		
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
	