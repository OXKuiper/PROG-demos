### test

import requests  # nodig voor http requests

## Dit is optioneel, maar netjes: Zet je wachtwoorden/keys in een losbestand die niet op github staat.
# Mijn key (in file die niet op github staat voor security)
with open('Data/my_openweather_key.txt') as file:
    api_key = file.read().strip()  # strip just in case

# bouw de URL
lat = "10"
lon = "10"
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

print(f'Gebruikte url is {url}')

response = requests.get(url)

# In response zit nu een python object waar verschillende informatie in zit
print(response) # dit geeft alleen de code terug  (200 = OK, 404 = verkeerde URL)
print(response.status_code) # geeft zelfde als bovenstaande

# dit is hoe je echt de data terugkrijgt (niet de code zoals 404)
response_data = response.json()

print(type(response_data)) # dict!
print(response_data) # dict, maar moeilijk te lezen zo

#Manier om het wat leesbaarder te maken:
for key in response_data.keys():
    print(f"{key}: {response_data[key]}")




