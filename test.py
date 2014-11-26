from articlesearch import ArticleSearch

if __name__ == '__main__':
    articlesearch = ArticleSearch()
    articlesearch.search_terms("new+york+times")
    articlesearch.set_return_fields("snippet,lead_paragraph")
    articlesearch.make_request()
    response = articlesearch.get_response()
    print response.text