import requests

#url = "http://localhost:8000/test"
url = "https://rcw-azzure-dadrgufpefhrecbq.canadaeast-01.azurewebsites.net/test"


response = requests.get(url)
try:
    response = response.json()
    print(response)
except Exception as e:
    print(e)
