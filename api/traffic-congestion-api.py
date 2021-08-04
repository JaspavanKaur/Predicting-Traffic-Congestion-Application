import numpy as np
import requests
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

model = pickle.load(open('../models/model.pkl', 'rb'))
curr = requests.get('http://127.0.0.1:5001/curr-weather').json()['data']
hourly = requests.get('http://127.0.0.1:5001/hour-forecast').json()['data']
daily = requests.get('http://127.0.0.1:5001/hour-forecast').json()['data']
features_col = ['month', 'day', 'hour', 'humidity', 'wind_speed', 'wind_direction', 'temp', 'clouds_all', 'weather_type']
# print([float(curr[feature]) for feature in features_col])

def predict_func(dic):
    features = [float(dic[feature]) for feature in features_col]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    return int(prediction[0])

# run the model to predict current, hourly forecast, daily forecast values
@app.route('/predict', methods=["GET"])
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