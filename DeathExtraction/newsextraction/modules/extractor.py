#TODO: create a class called DataExtractor to extract key information from the given news
from .tagger import Tagger
from .tokenizer import Tokenize
import nltk
import re

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
	
	def getDay(self, complete_news):
		""" Gets the day of mishap.
		"""
		day_regex = re.compile('\w+day')
		print(complete_news)
		day = day_regex.findall(complete_news)[0]
		# print("The day when the accident occured is: \n"+day)
		return day
	