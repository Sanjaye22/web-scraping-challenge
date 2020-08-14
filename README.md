# Web-scraping-challenge
# Mission to Mars


Objective: build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

* This challenge requires the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter. 

* Set up of Jupyter Notebook file called `mission_to_mars.ipynb` to complete scraping and analysis tasks. 

## Step 1 - Scraping

### NASA Mars News

* Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. 

### JPL Mars Space Images - Featured Image

* Visit the url for JPL Featured Space Image (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

* Make sure to find the image url to the full size `.jpg` image.

* Make sure to save a complete url string for this image.

### Mars Facts

* Visit the Mars Facts webpage (https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Visit the USGS Astrogeology site (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* Click each of the links to the hemispheres in order to find the image url to the full resolution image.

* Use a Python dictionary to store the data using the keys `img_url` and `title`.

* Append the dictionary with the image url string and the hemisphere title to a list. 

## Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Convert Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` to execute scraping code from above and return one Python dictionary containing all of the scraped data.

* Create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

* Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called `index.html` to take the mars data dictionary and display all of the data in the appropriate HTML elements. 


## Other considerations

* Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.

* Use Pymongo for CRUD applications for your database. 

* Use Bootstrap to structure your HTML template.


