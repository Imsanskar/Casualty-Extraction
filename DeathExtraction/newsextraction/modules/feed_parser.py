
import feedparser
from goose3 import Goose
import urllib
import requests
from requests import get





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
    extractor = Goose()
    for i in range(0, len(links)):
        #if links[i] not in oldlinks:
            response = get(links[i])
            
            article = extractor.extract(raw_html=response.content)
            texts = article.cleaned_text
            news_story = texts.encode('utf-8')
            print(news_story)
            
            # extract(links[i], news_story, title[i])       
