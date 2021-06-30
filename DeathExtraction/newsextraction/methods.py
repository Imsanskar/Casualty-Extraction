from hashlib import new

from nltk.util import pr
from modules.extractor import DataExtractor
from modules.tokenizer import Tokenize
from modules.tagger import Tagger
import nltk
import feedparser
from .models import *
from goose3 import Goose
import urllib
import requests
from requests import get
import re



#scrape rss feed
def initial_check():
    #print("here")
    url_link = "http://fetchrss.com/rss/60d9eed925c82c0cb439b71260d9ee245368013c620947d2.xml" # please create your own rss here
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
        news = Tokenize(news_story.decode('utf-8'))

    
    splited_sentences = news.sentences
    tokenized_words = news.words
    tagger = Tagger(tokenized_words)
    pos_tagged_sentences = tagger.getTaggedSentences()
    data_extractor = DataExtractor(pos_tagged_sentences, news_story)
    

    #change this later
    news_data = rssdata(header=title,
                     source="Kathmandu Post",
                     body=news_story.replace("\n", ""),
                     death=data_extractor.deaths(nltk.sent_tokenize(news_story)),
                     link=link,
                     injury_no=data_extractor.injury_number(),
                     death_no=data_extractor.death_number(),
                     location=data_extractor.location(),
                     injury=data_extractor.injury(nltk.sent_tokenize(news_story)),
                     date=date,
                     )
    news_data.save()
    return news_data.id
    