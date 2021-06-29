from hashlib import new

from nltk.util import pr
from modules.extractor import DataExtractor
from modules.tokenizer import Tokenize
from modules.tagger import Tagger
import nltk
import feedparser
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
    #parse the rss feed
    rss = feedparser.parse(url_link)
   
   #extract links, texts , titles in rss feed
    for post in rss.entries:
        links.append(post.link)
        
        title.append(post.title_detail.value)
        
    #oldlinks = rssdata.objects.values_list('link', flat=True) # need to link with models
    extractor = Goose()
    for i in range(0, len(links)):
        #if links[i] not in oldlinks:
            response = get(links[i])
            
            article = extractor.extract(raw_html=response.content)
            texts = article.cleaned_text
            news_story = texts.encode('utf-8')
            #print("tsest")
            
            extract(links[i], news_story, title[i])       


def extract(link, news_story, title):
    if isinstance(news_story, str):
        news = Tokenize(str(news_story, 'utf-8'))
    else:
        news = Tokenize(news_story.decode('utf-8'))

    
    #month, year, date = re.findall(r'\d+\S\d+\S\d+', news)
    splited_sentences = news.sentences
    tokenized_words = news.words
    tagger = Tagger(tokenized_words)
    pos_tagged_sentences = tagger.getTaggedSentences()
    #data_extractor = DataExtractor(pos_tagged_sentences, news_story)





    #change this later
    # record = rssdata(header=title,
    #                  source="Kathmandu Post",
    #                  body=news_story.replace("\n", ""),
    #                  death=data_extractor.deaths(nltk.sent_tokenize(news_story)),
    #                  link=link,
    #                  injury_no=data_extractor.injury_number(),
    #                  death_no=data_extractor.death_number(),
    #                  location=data_extractor.location(),
    #                  injury=data_extractor.injury(nltk.sent_tokenize(news_story)),
    #                  vehicle_type=vehicle_type,
    #                  
    #                  day=data_extractor.day(news_story),
    #                  date=date,
    #                  month=month,
    #                  year=year,
    #                  )

initial_check()