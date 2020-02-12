from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

mongo = "mongodb://localhost:27017/mars_data"


@app.route("/")
def index():

    mars_data = mongo.db.mars_data.find_one()

    return render_template("index.html", mars_data=mars_data)


@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars_data.update({}, mars_data, upsert=True)
    return 'All done!'

if __name__ == "__main__":
    app.run(debug=True)
