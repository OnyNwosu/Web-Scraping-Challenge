import datetime as dt
from bs4 import BeautifulSoup as soup 
from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


def scrape_all():
    # executable_path = {"executable_path": "/Users/ON054440/code/chromedriver"}
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)


    # Visit the mars nasa news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    slide_elem = news_soup.select_one('div.list_text')


    # Use the parent element to find the first a tag and save it as `news_title`
    news_title = slide_elem.find('div', class_='content_title').get_text()

    # Use the parent element to find the paragraph text
    news_paragraph = slide_elem.find('div', class_='article_teaser_body').get_text()

    # JPL Space Images

    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # find the relative image url
    img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    # Use the base url to create an absolute url
    featured_image = f'https://spaceimages-mars.com/{img_url_rel}'


    # Mars Facts

    df = pd.read_html('https://galaxyfacts-mars.com')[0]
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    mars_facts = df.to_html()
    
    hemispheres_list_of_dicts = [
        {"title": "Title of Hemisphere Image",
         "img_url": 'https://files.thefacecdn.com/images/_1200x630_crop_center-center_82_none/Bubbles_in_space.jpg?mtime=1612381004'},

        {"title": "Title of Hemisphere Image",
         "img_url": 'https://files.thefacecdn.com/images/_1200x630_crop_center-center_82_none/Bubbles_in_space.jpg?mtime=1612381004'},

        {"title": "Title of Hemisphere Image",
         "img_url": 'https://files.thefacecdn.com/images/_1200x630_crop_center-center_82_none/Bubbles_in_space.jpg?mtime=1612381004'},

        {"title": "Title of Hemisphere Image",
         "img_url": 'https://files.thefacecdn.com/images/_1200x630_crop_center-center_82_none/Bubbles_in_space.jpg?mtime=1612381004'},
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
