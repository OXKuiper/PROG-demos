### OMDB (film database) API voorbeeld

# Lees meer over hoe te gebruiken:
# https://www.omdbapi.com/#usage
# https://www.omdbapi.com/#parameters

import requests  # nodig voor http requests

## Dit is optioneel, maar netjes: Zet je wachtwoorden/keys in een losbestand die niet op github staat.
# Mijn key (in file die niet op github staat voor security)
with open('Data/my_omdbapi_key.txt') as file:
    api_key = file.read().strip()  # strip just in case

# api_key is bijvoorbeeld '8b03d282' (maar dan anders)
# bovenstaande with-open geeft iets als api_key='8b03d282'
# api_key = 'VUL HIER JOU KEY IN'


# bouw de URL met de api_key en waarop je wilt zoeken
search_term = 'Rocky'
url = f'http://www.omdbapi.com/?apikey={api_key}&t={search_term}'

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

### Extra: Schrijven naar JSON-bestand
import json # normaal zet je imports bovenaan .py-file
with open('Data/results.json', 'w') as json_file:
    # kijk een wat indent doet door weghalen of andere waarde
    json.dump(response_data, json_file, indent=5)




