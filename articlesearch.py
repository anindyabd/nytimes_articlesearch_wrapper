import os 
import requests 
from pprint import pprint


api_key = {'api-key': os.getenv('APIKEY')}

print(api_key)

r = requests.get(r'http://api.nytimes.com/svc/search/v2/articlesearch.json', params=api_key)

print(r.text) 

