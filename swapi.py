# Import dependencies
import requests
import json

base_url = "https://swapi.dev/api/people/"

character_id = '4'
url = base_url + character_id
response = requests.get(url)

data = response.json()
print(json.dumps(data, indent=4, sort_keys=True))
