from .models import *
import re

from modules.tagger import Tagger
from modules.extractor import DataExtractor
from modules.tokenizer import Tokenize
import en_core_web_sm #spacy.load('en_core_web_sm')
import nltk
import feedparser
from goose3 import Goose
from requests import get
from bs4 import BeautifulSoup
import urllib
import requests



nlp = en_core_web_sm.load()


#scrape rss feed
def initial_check():
    print("here")
    url_link = "http://fetchrss.com/rss/60d9eed925c82c0cb439b71260d9ee245368013c620947d2.xml" # please create your own rss here
    # get all the links of news title
    links = []
    text =[]
    title = []
    #parse the rss feed
    rss = feedparser.parse(url_link)
   
   #extract links, texts , titles in rss feed
    for post in rss.entries:
        links.append(post.link)
        
        title.append(post.title_detail.value)
        
    #oldlinks = rssdata.objects.values_list('link', flat=True) # need to link with models
    
    for i in range(0, len(links)):
        #if links[i] not in oldlinks:
            response = get(links[i])
            extractor = Goose()
            article = extractor.extract(raw_html=response.content)
            texts = article.cleaned_text
            news_story = texts.encode('utf-8')
        
            
            # extract(links[i], news_story, title[i])       
