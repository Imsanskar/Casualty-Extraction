from .models import *
import re

from .modules.tagger import Tagger
from .modules.tokenizer import Tokenize
import nltk
import feedparser
from goose3 import Goose
from requests import *
from bs4 import BeautifulSoup
import urllib
import requests
from .modules.extractor import DataExtractor

"""
	Extracts the info from the news story extracted using scrapper
	Input:
		newsStory: string from which info is to be extracted
	Returns: Data Extractor object which contains methods object to extract the data
"""
def extractInfo(newsStory:str) -> DataExtractor:
	# tokenizer object
	newsTokenize = Tokenize(newsStory)

	# sentence and word token of the news
	sentenceToken = newsTokenize.sentenceTokenize()
	wordToken = newsTokenize.wordTokenize()

	# pos tagging of the tokenized objects
	posTagger = Tagger(sentenceToken)
	posTagedSentences = posTagger.tags()

	# data extractor object which contains methods object to extract the data
	extractedData = DataExtractor(posTagedSentences, newsStory)

	# sentences = newsStory.split()
	return extractedData


	
