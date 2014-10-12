import os 
import requests 

class ArticleSearch(object): 

    base_url = r'http://api.nytimes.com/svc/search/v2/articlesearch.'

    response_format = 'json'

    api_key = os.getenv('APIKEY')

    response = ""

    params = {'api-key':api_key, 'q': 'Obama'}

    def __init__(self, query_dict=None):
        pass 

    def set_api_key(self, api_key):
        self.api_key = api_key

    def set_format(self, format_str):
        """
        Set a specific format for the response (json or jsonp).
        Default is json.
        """
        if format_str != 'json' or format_str != 'jsonp':
            raise ValueError("Wrong format.")
        self.response_format = format_str  

    def make_request(self):
        request_url = self.base_url + self.response_format
        self.response = requests.get(request_url, params=self.params)
        print self.response.text 

# Testing 
if __name__ == '__main__':
    articlesearch = ArticleSearch()
    articlesearch.make_request()
