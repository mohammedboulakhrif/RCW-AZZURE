import requests

url = "http://localhost:8000/test"

response = requests.post(url)

print(response.json())