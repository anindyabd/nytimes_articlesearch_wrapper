import os 
import requests  

class ArticleSearch(object): 

    # The base_url is shared across all instances of ArticleSearch
    base_url = r'http://api.nytimes.com/svc/search/v2/articlesearch.'

    def __init__(self, params=None, response_format=None):
        """ Initializes the ArticleSearch class.
        Queries for the API call can either be passed as a dictionary
        using the `params` parameter when initializing the class, or they 
        can be set separately with the `set` methods."""
        if response_format == None:
            self.response_format = 'json' # default response format 
        else:
            self.response_format = response_format 
        if params != None:
            self.params = params 
        else:
            self.params = {} 
            self.response_format = 'json' 
            
            self.params['api-key'] = os.getenv('API_KEY') 
            self.made_request = False

    def set_api_key(self, api_key):
        """
        Set the API key for your ArticleSearch object.
        """
        self.params['api_key'] = api_key

    def set_format(self, format_str):
        """
        Set a specific format for the response (json or jsonp).
        Default is json.
        """
        if format_str != 'json' or format_str != 'jsonp':
            raise ValueError("Wrong format.")
        self.response_format = format_str 

    def search_terms(self, q):
        """
        Enter the search-query terms. It should be one string.
        Instead of spaces, put in + sign to separate words, e.g. new+york+times.
        """
        self.params['q'] = q 

    def set_return_fields(self, fields):
        """
        Sets the return fields specified in the fields parameter. fields 
        should be a string containing the fields delimited by commas; no spaces allowed.
        """
        self.params['fl'] = fields

    def make_request(self):
        params = self.params
        request_url = self.base_url + self.response_format
        self.response = requests.get(request_url, params=params)
        self.made_request = True
        
    def get_response(self):
        """
        Get the response object associated with this instance of your ArticleSearch object.
        """
        if not self.made_request:
            return "You didn't make an API call yet! Make a request with the make_request() method."
        return self.response

    def get_decoded_response(self):
        """
        Get the decoded response.
        """
        if not self.made_request:
            return "You didn't make an API call yet! Make a request with the make_request() method."
        return self.response.json()

    
