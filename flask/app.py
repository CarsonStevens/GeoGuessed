import pandas as pd
from flask import Flask, jsonify, request
import pickle
from  config 

# app
app = Flask(__name__)

# routes
@app.route('/', methods = ['POST'])

def predict():
    # get data
    # data = request.get_json(force = True)

    # convert into dataframe
    
    # predictions
    result = None

    # send back to browser
    output = {
        'results': None
    }

    # return data
    return jsonify(results = output)

if __name__ == '__main__':
    app.run(port = config.FLASK_PORT, debug = debug_status)
