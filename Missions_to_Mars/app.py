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

# create route that renders index.html template
@app.route("/")
def home():

    # Find data
    mars_info = db.mars.find_one()
    print(mars_info)

    # Return template and data
    return render_template("index.html", mars_info=mars_info)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape()
    
    # Update the Mongo database using update and upsert=True
    db.mars.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
