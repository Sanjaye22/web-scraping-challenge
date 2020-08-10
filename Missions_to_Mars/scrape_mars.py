#Dependencies
import pandas as pd
from pandas import *
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = bs(html)

    #News ttile and paragraph
    news_title = soup.find_all("div", class_="content_title")[1].text
    news_p = soup.find("div", class_="article_teaser_body").text

    #Featured Image   
    jpl_url = "https://www.jpl.nasa.gov"
    images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(images_url)
    time.sleep(1)

    html = browser.html
    img_soup = bs(html, "html.parser")

    img_link = img_soup.find("a", id="full_image")["data-fancybox-href"]
    featured_image_url = jpl_url + img_link
    
    #Mars Facts
    mars_facts_url = "https://space-facts.com/mars/"
    mars_facts_tables = pd.read_html(mars_facts_url)[0]
    mars_facts_tables

    df = mars_facts_tables
    df.columns = ["Description", "Values"]
    df.head()

    #Convert Table to HTML
    html_table = df.to_html()
    html_table

    html_table.replace('\n', '')

    #Mars_hemispheres 
    usgs_url = 'https://astrogeology.usgs.gov'
    hemisphere_image_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_image_url)
    time.sleep(1)

    # Iterate through each hemisphere data
    for x in range(4):
        
        #html object
        html = browser.html

        #Parse HTML with Beautiful Soup
        images_soup = bs(html, "html.parser")

        mars_hemispheres = images_soup.find('div', class_='collapsible results')
        mars_hemispheres_1 = mars_hemispheres.find_all('div', class_='item')

        hems_image_urls = []


    for mar in mars_hemispheres_1:
    # Collect Title
        m_hems = mar.find('div', class_="description")
        title = m_hems.h3.text
    
    # Collect image link by browsing to hemisphere page
        hemisphere_link = m_hems.a["href"]    
        browser.visit(usgs_url + hemisphere_link)

        image_html = browser.html
        image_soup = bs(image_html, 'html.parser')

        image_link = image_soup.find('div', class_='downloads')
        image_url = image_link.find('li').a['href']

    # Create Dictionary to store title and url info
        image_dict = {}
        image_dict['title'] = title
        image_dict['img_url'] = image_url

        hems_image_urls.append(image_dict)

        m_dict ={
                "news_title": news_title,
                "news_p": news_p,
                "featured_image_url": featured_image_url,
                "fact_table": str(html_table),
                "hemisphere_images": hems_image_urls
            }
        m_dict

    # Close the browser after scraping
    browser.quit()

    # Return results
    return m_dict


