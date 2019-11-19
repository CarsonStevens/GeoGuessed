import cnn
import pickle
from app import *
import pandas as pd
from config import *
from flask import Flask, jsonify, request, render_template

# webserver
server = Flask(__name__)
server.config['TESTING'] = True

img_dir = "../images/10k"
app = App()
#app.load_images(directory = img_dir)

#boot()

## ROUTES
@server.route('/', methods = ['GET'])
def hello():
    return render_template("index.html")

# receive a photo and store in sequence
# note: will be folded into /predict once the full game is ready
@server.route('/put/image', methods = ['POST'])
def put_image():
    try:
        # data = request.get_json(force = True)
        data = request.get_json(force = True)
        sequence_id = data['sequence_id']
        image_url = data['image_url']
        lat = data['lat']
        lng = data['lng']
        # print(f"sequence_id: {sequence_id},\nimage_url: {image_url},\nlat: {lat},\nlng: {lng}")
        #
        if app.save_streetview_image(sequence_id = sequence_id,
                                     image_url = image_url,
                                     lat = lat,
                                     lng = lng
                                    ):
            return jsonify({
                "status": "200",
                "result": "1"
            })
        else:
            return jsonify({
                "status": "200",
                "result": "0"
            })

    except Exception as e:
        print(f"put_image error {e}")
        return jsonify({
            "message": f"error: {e}"
        })


@server.route('/predict', methods = ['POST'])
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
    server.run(host = "0.0.0.0", port = 5000, debug = True)
