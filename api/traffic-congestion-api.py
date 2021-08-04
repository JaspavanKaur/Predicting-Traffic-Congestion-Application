import numpy as np
import requests
import pickle
# from datetime import date
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

model = pickle.load(open('../models/model.pkl', 'rb'))
curr = requests.get('http://127.0.0.1:5001/curr-weather').json()['data']
hourly = requests.get('http://127.0.0.1:5001/hour-forecast').json()['data']
daily = requests.get('http://127.0.0.1:5001/daily-forecast').json()['data']
features_col = ['month', 'day', 'hour', 'humidity', 'wind_speed', 'wind_direction', 'temp', 'clouds_all', 'weather_type']
# print([float(curr[feature]) for feature in features_col])

def predict_func(dic):
    features = [float(dic[feature]) for feature in features_col]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    if int(prediction[0]) == 0:
        result = "Low"
        colour = "success"
    elif int(prediction[0]) == 1:
        result = "Medium"
        colour = "warning"
    else:
        result = "High"
        colour = "danger"
    # print(dic['date'])
    return {'date': dic['date'], 'time': dic['time'], 'prediction':int(prediction[0]),'result': result, 'colour': colour}

# run the model to predict current, hourly forecast, daily forecast values
@app.route('/predict', methods=["GET"])
@cross_origin()

def predict():
    #predict current congestion
    return jsonify(
        {
            "code": 200,
            "data": {
                "current": predict_func(curr),
                "hourly": [predict_func(dich) for dich in hourly],
                "daily": [predict_func(dicd) for dicd in daily]
            }
        }
    )

if __name__ == "__main__":
    app.run(port=5003, debug=True)