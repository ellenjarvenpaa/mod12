import requests
import json

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
data = response.json()
print(data['value'])

