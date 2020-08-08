from flask import Flask, render_template, redirect
import pymongo
import scrape_mars
# from flask_pymongo 

# Create an instance of Flask
app = Flask(__name__)

# Create connection variable
conn = "mongodb://localhost:27017"

#Pass connection to the pymongo instance
client = pymongo.MongoClient(conn)

#Set database
db = client.mars_db

#Drops collection if available to remove duplicates
db.mars.drop()

# create route that renders index.html template
@app.route("/")
def home():

    # Find data
    mars_info = mongo.db.mars_info.find()

    # Return template and data
    return render_template("index.html", mars_info=mars_info)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.mars_info
    mars_data = scrape_mars.scrape_mars_news()
    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
