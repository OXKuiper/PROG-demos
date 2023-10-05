# Lees meer over hoe te gebruiken:
# https://www.omdbapi.com/#usage
# https://www.omdbapi.com/#parameters

import requests  # nodig voor http requests
import json      # nodig voor json bestanden

# Mijn key (in file die niet op github staat voor security)
with open('Data/my_omdbapi_key.txt') as file:
    api_key = file.read().strip()  # strip just in case

# api_key is bijvoorbeeld '8b03d282' (maar dan anders)

search_term = 'Rocky'
# bouw de URL met de api_key en waarop je wilt zoeken
url = f'http://www.omdbapi.com/?apikey={api_key}&t={search_term}'

print(f'Gebruikte url is {url}')


response = requests.get(url)
print(response) # dit geeft alleen de code terug  (200 = OK)

data = response.json()
print(data)

