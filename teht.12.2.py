import requests
import json

paikkakunta = input("Anna paikkakunta: ")
url = f"api.openweathermap.org/data/2.5/weather?q={paikkakunta},uk&APPID=4df407ab93b36ceb0a5be640f6004d9a"
response = requests.get(url)
data = response.json()

print(data['weather']['temp'])
