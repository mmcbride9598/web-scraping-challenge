from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape():

    browser = init_browser()
    mars_url = 'https://mars.nasa.gov/news/'

    response = requests.get(mars_url)
    soup = bs(response.text, 'html.parser')

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    featured_image_url = '/spaceimages/images/mediumsize/PIA14417_ip.jpg'

    facts_url = 'https://space-facts.com/mars/'

    space_facts.html

    hemisphere_image_urls = [
    {"title" : "Cerberus Hemisphere","img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title" : "Schiaparelli Hemisphere","img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title" : "Syrtis Major  Hemisphere","img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    {"title" : "Valles Marineris  Hemisphere","img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
]
