import datetime as dt
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.mars_db
collection = db.mars

def init_browser():
    executable_path = {"executable_path": "/Users/ON054440/Downloads/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)




def scrape_all():

    news_title = 'Testing'
    news_paragraph = 'Testing'
    featured_image = 'https://linktoimage.png'
    mars_facts = 'Testing'
    news_title = 'Testing'
    hemispheres_list_of_dicts = [
        {"title": "Title of Hemisphere Image",
        "img_url": 'https://linktoimage.png'},

        {"title": "Title of Hemisphere Image",
        "img_url": 'https://linktoimage.png'},

        {"title": "Title of Hemisphere Image",
        "img_url": 'https://linktoimage.png'},
        
        {"title": "Title of Hemisphere Image",
        "img_url": 'https://linktoimage.png'},
    ]

    scraped_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image,
        "facts": mars_facts,
        "hemispheres": hemispheres_list_of_dicts,
        "last_modified": dt.datetime.now()
    }

    return scraped_data