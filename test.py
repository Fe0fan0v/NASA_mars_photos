import requests
from pprint import pprint

API_KEY = 'JBuGtYcdod8udN03Io2XfuD5FejXbhYvwWUkwE2y'
params = {'api_key': API_KEY}
resp = requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/', params=params).json()['rover']['max_sol']
pprint(resp)




