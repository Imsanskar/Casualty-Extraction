from newsextraction.modules.vehicles_gazetter import VehicleInformation
from newsextraction.modules.wordNum import text2int
from newsextraction.modules.deathinjury import death_no, injury_no
from ..models import *
import re

from .tagger import Tagger
from .tokenizer import Tokenize
import nltk
import feedparser
from goose3 import Goose
from requests import *
from bs4 import BeautifulSoup
import urllib
import requests
from .extractor import DataExtractor
from dateutil.parser import parse

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

#scrape rss feed
def initial_check():
	url_link = "https://rss.app/feeds/NZxckjuk8A0VhGpG.xml"
	# create your own rss here
	# get all the links of news title
	links = []
	text =[]
	title = []
	date=[]
	source = []
	#parse the rss feed
	rss = feedparser.parse(url_link)
   
   #extract links, texts , titles in rss feed
	for post in rss.entries:
		if post.has_key('published'):
			links.append(post.link)
			date.append(post.published)
			title.append(post.title_detail.value)
			source.append(post.author)
		
	oldlinks = rssdata.objects.values_list('link', flat=True) # need to link with models
	
	extractor = Goose()
	for i in range(0, len(links)):
		if links[i] not in oldlinks:
			response = get(links[i])
			
			article = extractor.extract(raw_html=response.content)
			texts = article.cleaned_text
			texts = texts.replace("\xe2\x80\x9c", " ").replace("\xe2\x80\x9d", " ").replace("\n\n"," ").replace("xe2\x80\x99s"," ")
			news_story = texts.encode('utf-8')
			
			
			extract(links[i], texts, title[i],date[i], source[i])       

#Apply tokenization and tagging
def extract(link, news_story, title, date, source, save = True):

	news = Tokenize(news_story)
	splited_sentences = news.sentences
	tokenized_words = news.words
	tagger = Tagger(tokenized_words)
	pos_tagged_sentences = tagger.getTaggedSentences()
	data_extractor = DataExtractor(pos_tagged_sentences, news_story,title)
	vehicleGazetter = VehicleInformation(news_story)
	
	news_date = ""
	if(date != ""):
		news_date  = parse(date)
	month_list = [ "January", "February", "March", "April", "May", "June",
"July", "August", "September", "October", "November", "December" ];

	vehicles, isTwo, isThree, isFour = vehicleGazetter.find_vehicles()

<<<<<<< Updated upstream
	#change this later
=======

	deathNo = death_no(news_story, str(title))
	injuryNo = injury_no(news_story, str(title))


	deathNumber = 0
	injuryNumber = 0
	try:
		deathNumber = int(text2int(deathNo))
	except ValueError:
		deathNumber = convertNum(deathNo)


	try:
		injuryNumber = int(text2int(injuryNo))
	except ValueError:
		injuryNumber = convertNum(injuryNo)
	
	# oldlink so that news are not duplicated
	oldlinks = rssdata.objects.values_list('link', flat=True) # need to link with models

	if link in oldlinks:
		save = False


>>>>>>> Stashed changes
	news_data = rssdata(header=title,
					 source=source,
					 body=str(news_story),
					 death=death_no(news_story, str(title)),
					 injury=injury_no(str(news_story), str(title)),
					 link=link,
					 location=data_extractor.getLocation(),
					 date=date,
					 month = month_list[news_date.month - 1] if date != "" else "",
					 year = news_date.year if date != "" else "",
					 day = news_date.day if date != "" else "",
					 vehicleNo = len(vehicles),
					 vehicleCode = data_extractor.vehicle(),
					 vehicleType = vehicles
					 )
	
	if save:	
		news_data.save()
	return news_data
	
