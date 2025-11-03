import requests

response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")

print(response)