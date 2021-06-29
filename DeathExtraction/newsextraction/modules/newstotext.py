#TODO: create a class called extractor to extract news_story

import requests
from bs4 import BeautifulSoup
from extractor import DataExtractor

    
def story_extract(link:str):
    """
    Input :link
    Output:Return news_title  story and link
    Html extraction using beautiful soup and requests
    """
    story=""
    html_text=requests.get(link).text
    soup=BeautifulSoup(html_text,'html.parser')
    for paragraph in soup.find_all('p'):
        story += paragraph.text
    return soup.title.text,story,link



title,news_story,link=(story_extract('https://myrepublica.nagariknetwork.com/news/more-than-50-people-missing-in-melamchi-flood/'))
DataExtract= DataExtractor(news_story)
print(DataExtract.getLocation())
print(DataExtract.getDeathNumber())
print(DataExtract.getInjuryNumber())