import os 
import requests  

class ArticleSearch(object): 

    base_url = r'http://api.nytimes.com/svc/search/v2/articlesearch.'

    response_format = 'json' 

    api_key = os.getenv('API_KEY')

    response = ""

    params = None 

    q = ""

    fl = ""

    made_request = False


    def __init__(self, params=None):
        """ Initializes the ArticleSearch class.
        Queries for the API call can either be passed as a dictionary
        to the initializer to the `params` parameter, or the queries 
        can be set separately with the `set` methods."""
        if params != None:
            self.params = params 


    def set_api_key(self, api_key):
        """
        Set the API key for your ArticleSearch object.
        """
        self.api_key = api_key

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
        self.q = q 

    def set_return_fields(self, fields):
        """
        Sets the return fields specified in the fields parameter. fields 
        should be a string containing the fields delimited by commas; no spaces allowed.
        """
        self.fl = fields

    def make_request(self):
        if self.params == None:
            params = {'api-key': self.api_key, 'q': self.q, 'fl':self.fl}
        else:
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

    
# Example: 
if __name__ == '__main__':
    articlesearch = ArticleSearch()
    articlesearch.search_terms("new+york+times")
    articlesearch.set_return_fields("snippet,lead_paragraph")
    articlesearch.make_request()
    decoded_response = articlesearch.get_decoded_response()
    print decoded_response
