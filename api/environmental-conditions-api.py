import requests
import calendar
import datetime

lat = 1.3521
long = 103.8198
api_key = "964fdadc10dc2dd84876ffe6927b90bf"

#retrieve date and check if date is holiday or not
date_time = datetime.datetime.utcnow()
utc = calendar.timegm(date_time.utctimetuple())

#weather current, historical, future data
res_weather = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(long)+"&exclude=minutely&appid="+api_key).json()
res_weather_hist = requests.get("https://api.openweathermap.org/data/2.5/onecall/timemachine?lat="+str(lat)+"&lon="+str(long)+"&dt="+str(utc)+"&appid="+api_key).json()

#air pollution current, historical, future data
res_ap_curr = requests.get("http://api.openweathermap.org/data/2.5/air_pollution?lat="+str(lat)+"&lon="+str(long)+"&appid="+api_key).json()
res_ap_forecast = requests.get("http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat="+str(lat)+"&lon="+str(long)+"&appid="+api_key).json()
res_ap_hist = requests.get("https://api.openweathermap.org/data/2.5/onecall/timemachine?lat="+str(lat)+"&lon="+str(long)+"&dt="+str(utc)+"&appid="+api_key).json()

