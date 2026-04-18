## Day 9 APIs & JSON ##

import requests

# first API request

url = "https://api.open-meteo.com/v1/forecast?latitude=42.3&longitude=-83.0&current_weather=true"
response = requests.get(url)

print(response.status_code)  # status_code tells us whether the API request was successful or not.
print(type(response))


data = response.json()  # converts JSON to a python dictionary
print(data)

# 'data' full dictionary for the API and this accesses the 'currect_weather' key which gives us some key variables #
weather = data["current_weather"]
temp = weather["temperature"]
wind = weather["windspeed"]

print(f"Current temperature: {temp}°C")
print(f"Wind speed: {wind} km/h")
