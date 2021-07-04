#TODO: create a class called DataExtractor to extract key information from the given news
from .tagger import Tagger
from .tokenizer import Tokenize
import nltk

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
	
	def getDate(self, sentences):
		""" Gets the number of deaths from the news story.
			Inputs include the POS tagged words from the news story.
			Output includ the number of deaths mentioned in the news.
		"""
		death_words = ["died", "death", "killed", "life"]
		# death_regex = "Deaths: {<NNP>?<CD><NNS|NNP>?<VBD|VBN>?<VBD|VBN>}"
		death_regex = "Deaths: {<CD>}"
		has_deaths = [sent for sent in sentences if ("died" or "death") in nltk.word_tokenize(sent)]
	
		death_parser = nltk.RegexpParser(death_regex)

		for i in self.posTaggedSentences:
			deaths = death_parser.parse(i)
			for i in deaths.subtrees(filter=lambda x: x.label() == 'Deaths'):
				# print(i.leaves())
				pass
	
	def getDeathNumber(self):
		raise NotImplementedError
	
	def getInjuryNumber(self):
		raise NotImplementedError
	