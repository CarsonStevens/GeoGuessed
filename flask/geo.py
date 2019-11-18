import pandas as pd
from flask import Flask, jsonify, request, render_template
import pickle
from config import *
import cnn
# app
app = Flask(__name__)
app.config['TESTING'] = True

# routes
@app.route('/', methods = ['GET'])
def hello():
    # return 'Welcome to GeoGuessed!'
    # return render_template("index.html", message="Hello Flask!"); 
    return render_template("index.html")

@app.route('/predict', methods = ['POST'])
def predict():
    # get data
    data = request.get_json(force = True)
    print("r: ", data)

    # predictions example
    command = "predict"
    prediction = (0.0, 0.0)

    # send back to browser
    output = {
        'command'    : command,
        'prediction' : prediction
    }

    # return data
    return jsonify(results = output)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000, debug = True)
