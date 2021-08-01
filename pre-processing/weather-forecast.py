import requests

response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=1.3521&lon=103.8198&exclude=minutely&appid=964fdadc10dc2dd84876ffe6927b90bf")

print(response.json())