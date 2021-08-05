import requests
import datetime
import statistics

from flask import Flask, request, jsonify

app = Flask(__name__)

lat = 1.3521
long = 103.8198
api_key = "964fdadc10dc2dd84876ffe6927b90bf"

weather_map = {
    'Clouds':1,
    'Clear':2, 
    'Mist':3, 
    'Rain':4, 
    'Snow':5, 
    'Drizzle':6, 
    'Haze':7,
    'Fog':8,
    'Thunderstorm':9,
    'Smoke':10,
    'Squall':11
}

#get month, day, hour
def retrieve_datetime(unix):
    # unix = res_weather["current"]["dt"]
    month = datetime.datetime.utcfromtimestamp(unix).strftime('%m')
    day = datetime.datetime.utcfromtimestamp(unix).strftime('%d')
    hour = datetime.datetime.utcfromtimestamp(unix).strftime('%H')
    return month, day, hour

#api that retrieves current weather data for testing
@app.route('/curr-weather', methods=['GET'])
def current():
    res_weather = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(long)+"&exclude=minutely,alerts&appid="+api_key).json()
    curr_weather = res_weather['current']
    weather_type = curr_weather['weather'][0]['main']
    date_time = retrieve_datetime(curr_weather["dt"])
    if len(curr_weather):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "date": datetime.datetime.fromtimestamp(curr_weather['dt']).strftime('%A, %d %B %Y'),
                    "time": datetime.datetime.fromtimestamp(curr_weather['dt']).strftime('%H:%M:%S'),
                    "month":date_time[0],
                    "day":date_time[1],
                    "hour":date_time[2],
                    "temp":curr_weather['temp'],
                    "humidity":curr_weather['humidity'],
                    "wind_speed":curr_weather['wind_speed'],
                    "wind_direction":curr_weather['wind_deg'],
                    "clouds_all":curr_weather['clouds'],
                    "weather_type":weather_map[weather_type]
                }
            }
        )
    return jsonify( #return in http request
        {
            "code": 404,
            "message": "There is an error on retrieving current weather data."
        }
    ), 404

#api that retrieves hourly forecast data for testing
@app.route('/hour-forecast', methods=['GET'])
def hour():
    res_weather = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(long)+"&exclude=minutely,alerts&appid="+api_key).json()
    hourly_forecast = res_weather['hourly']
    forecast_list = []
    for forecast in hourly_forecast:
        weather_type = forecast['weather'][0]['main']
        date_time = retrieve_datetime(forecast["dt"])
        forecast_list.append({
            "date": datetime.datetime.fromtimestamp(forecast['dt']).strftime('%A, %d %B %Y'),
            "time": datetime.datetime.fromtimestamp(forecast['dt']).strftime('%H:%M:%S'),
            "month":date_time[0],
            "day":date_time[1],
            "hour":date_time[2],
            "temp":forecast['temp'],
            "humidity":forecast['humidity'],
            "wind_speed":forecast['wind_speed'],
            "wind_direction":forecast['wind_deg'],
            "clouds_all":forecast['clouds'],
            "weather_type":weather_map[weather_type]
        })
    if len(hourly_forecast):
        return jsonify(
            {
                "code": 200,
                "data": forecast_list
            }
        )
    return jsonify( #return in http request
        {
            "code": 404,
            "message": "There is an error on retrieving forecast weather data."
        }
    ), 404

#api that retrieves daily forecast data for testing
@app.route('/daily-forecast', methods=['GET'])
def daily():
    res_weather = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(long)+"&exclude=minutely,alerts&appid="+api_key).json()
    daily_forecast = res_weather['daily']
    forecast_list = []
    for forecast in daily_forecast:
        weather_type = forecast['weather'][0]['main']
        date_time = retrieve_datetime(forecast["dt"])
        forecast_list.append({
            "date": datetime.datetime.fromtimestamp(forecast['dt']).strftime('%A, %d %B %Y'),
            "time": datetime.datetime.fromtimestamp(forecast['dt']).strftime('%H:%M:%S'),
            "month":date_time[0],
            "day":date_time[1],
            "hour":date_time[2],
            "temp":statistics.mean(list(forecast['temp'].values())),
            "humidity":forecast['humidity'],
            "wind_speed":forecast['wind_speed'],
            "wind_direction":forecast['wind_deg'],
            "clouds_all":forecast['clouds'],
            "weather_type":weather_map[weather_type]
        })
    if len(daily_forecast):
        return jsonify(
            {
                "code": 200,
                "data": forecast_list
            }
        )
    return jsonify( #return in http request
        {
            "code": 404,
            "message": "There is an error on retrieving forecast weather data."
        }
    ), 404

if __name__ == "__main__":
    app.run(port=5001, debug=True)