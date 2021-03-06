from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.lyft_data

# Create an instance of our Flask app.
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# # Set route
@app.route('/')
def index():
    return "please visit the api routes"

@app.route('/api/lyft_sept_2014')
@cross_origin()
def lyft_sept_2014():
    cs_info = [doc for doc in db.sept_5.find({}, {'_id': False})]
    cs_info_format = {"data": cs_info}
    # print(cs_info)
    return jsonify(cs_info_format)

if __name__ == "__main__":
    app.run(debug=True)