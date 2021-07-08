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
	
	url_link = "https://rss.app/feeds/L0VeKbLXpidVMd8A.xml" # please create your own rss here
	# get all the links of news title
	links = []
	text =[]
	title = []
	date=[]
	#parse the rss feed
	rss = feedparser.parse(url_link)
   
   #extract links, texts , titles in rss feed
	for post in rss.entries:
		links.append(post.link)
		date.append(post.published)
		title.append(post.title_detail.value)
		
	oldlinks = rssdata.objects.values_list('link', flat=True) # need to link with models
	
	extractor = Goose()
	for i in range(0, len(links)):
		if links[i] not in oldlinks:
			response = get(links[i])
			
			article = extractor.extract(raw_html=response.content)
			texts = article.cleaned_text
			news_story = texts.encode('utf-8')
			
			
			extract(links[i], news_story, title[i],date[i])       

#Apply tokenization and tagging
def extract(link, news_story, title,date):
	if isinstance(news_story, str):
		news = Tokenize(str(news_story, 'utf-8'))
	else:
		news = Tokenize(news_story.decode('utf-8').replace("\xe2\x80\x9c", "").replace("\xe2\x80\x9d", "").replace("\n\n","").replace("xe2\x80\x99s",""))

	
	splited_sentences = news.sentences
	tokenized_words = news.words
	tagger = Tagger(tokenized_words)
	pos_tagged_sentences = tagger.getTaggedSentences()
	data_extractor = DataExtractor(pos_tagged_sentences, news_story,title)
	

	#change this later
	news_data = rssdata(header=title,
					 source="Kathmandu Post",
					 body=str(news_story).encode('ascii', errors='ignore').decode("utf-8"),
					 death=death_no(str(news_story)),
					 link=link,
					#  injury_no=data_extractor.injury_number(),
					#  death_no= int(text2int(death_no(str(news_story)))),
					 location=data_extractor.getLocation(),
					#  injury=data_extractor.injury(nltk.sent_tokenize(news_story)),
					 date=date,
					 )
	
	
	news_data.save()
	return news_data.id
	
