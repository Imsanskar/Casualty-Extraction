from newsextraction.modules.locationTree import LocationInformation
from django.db.models.expressions import Value
from newsextraction.modules.vehicles_gazetter import VehicleInformation
from newsextraction.modules.wordNum import text2int
from newsextraction.modules.deathinjury import death_no, injury_no
from ..models import *
import re
from newsextraction.modules.wordNum import *
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
	if(len(news_story) == 0 or len(title) == 0):
		return None

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
	
	#change this later
	news_data = rssdata(header=title,
					 source=source,
					 body=str(news_story),
					 death=deathNo,
					 injury=injuryNo,
					 death_no = deathNumber,
					 injury_no = injuryNumber,
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
	
def getLocations():
	"""import all location from database"""
	listoflocation = rssdata.objects.values('location').order_by('location')

	""" import all location from kathmandu, bhaktapur, lalitpur and outside from location_tree.py """
	ktm_location = LocationInformation().all_ktm_locations()
	bkt_location = LocationInformation().all_bkt_locations()
	ltp_location = LocationInformation().all_ltp_locations()
	outside_location = LocationInformation().all_locations()

	""" list definition"""
	alllocationlist = []
	ktmlocationlist = []
	ltplocationlist = []
	bktlocationlist = []
	outsideLocationList = []

	"""
		Dictionary to store the no of accidents according to the districts
	"""
	locationCount = {}

	for findlocation in listoflocation:

		""" check if defined location is in kathmandu or lalitpur or bhaktapur or others"""
		if findlocation['location'] in ktm_location:
			""" add location to kathmandu location list and
			add kathmandu to all location"""
			ktmlocationlist.append({'location': findlocation['location'].capitalize()})
			if 'Kathmandu' not in alllocationlist:
				alllocationlist.append('Kathmandu')
				locationCount['Kathmandu'] = 1
			else:
				locationCount['Kathmandu'] += 1
			

		elif findlocation['location'] in ltp_location:
			""" add location to Lalitpur location list and
			add Lalitpur to all location"""
			ltplocationlist.append(findlocation['location'].capitalize())
			if 'Lalitpur' not in alllocationlist:
				alllocationlist.append('Lalitpur')
				locationCount['Lalitpur'] = 1
			else:
				locationCount['Lalitpur'] += 1

		elif findlocation['location'] in bkt_location:
			""" add location to Bhaktapur location list and
				add Bhaktapur to all location"""
			bktlocationlist.append(findlocation['location'].capitalize())
			if 'Bhaktapur' in alllocationlist:
				alllocationlist.append('Bhaktapur')
				locationCount['Bhaktapur'] = 1
			else:
				locationCount['Bhaktapur'] += 1

		elif findlocation['location'] in outside_location:
			alllocationlist.append(findlocation['location'].capitalize())
			if findlocation['location'] not in locationCount:
				locationCount[findlocation['location']] = 1
			else:
				locationCount[findlocation['location']] += 1

		else:
			outsideLocationList.append(findlocation['location'].capitalize())

	return alllocationlist, ktmlocationlist, ltplocationlist, bktlocationlist, outsideLocationList, locationCount


def getDeathCountLocation():
	"""
		Returns the death count of the particular location 
	"""
	querySet = rssdata.objects.values('location', 'death_no')

	""" import all location from kathmandu, bhaktapur, lalitpur and outside from location_tree.py """
	ktm_location = LocationInformation().all_ktm_locations()
	bkt_location = LocationInformation().all_bkt_locations()
	ltp_location = LocationInformation().all_ltp_locations()
	outside_location = LocationInformation().all_locations()

	deathCount = {}

	#traverse through all the location
	for findlocation in querySet:

		""" check if defined location is in kathmandu or lalitpur or bhaktapur or others"""
		if findlocation['location'] in ktm_location:
			if 'Kathmandu' not in deathCount:
				deathCount['Kathmandu'] = findlocation['death_no']
			else:
				deathCount['Kathmandu'] += findlocation['death_no']
			

		elif findlocation['location'] in ltp_location:
			if 'Lalitpur' not in deathCount:
				deathCount.append('Lalitpur')
				deathCount['Lalitpur'] = findlocation['death_no']
			else:
				deathCount['Lalitpur'] += findlocation['death_no']

		elif findlocation['location'] in bkt_location:
			if 'Bhaktapur' in deathCount:
				deathCount.append('Bhaktapur')
				deathCount['Bhaktapur'] = findlocation['death_no']
			else:
				deathCount['Bhaktapur'] += findlocation['death_no']

		elif findlocation['location'] in outside_location:
			if findlocation['location'] not in deathCount:
				deathCount[findlocation['location']] = findlocation['death_no']
			else:
				deathCount[findlocation['location']] += findlocation['death_no']

	return deathCount


	
