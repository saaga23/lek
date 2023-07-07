from flask import Flask, request, jsonify
from flask_frozen import Freezer

import util

app = Flask(__name__)
freezer = Freezer(app)

@app.route("/get_location_names")
def get_location_names():
    response = jsonify({
        "location": util.get_location_names()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    bedrooms = float(request.form['bedrooms'])
    house_type = request.form['house_type']
    parking_space = float(request.form['parking_space'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(bedrooms, parking_space, house_type)
    })

    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

if __name__ == '__main__':
    app.testing = True  # Set testing to True for Frozen-Flask
    app.config['FREEZER_DESTINATION'] = 'build'  # Specify the output directory for static files

    util.load_saved_artifects()  # Load artifacts before freezing

    freezer.freeze()  # Generate static files

    app.run()
