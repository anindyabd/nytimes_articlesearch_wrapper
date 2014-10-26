NY Times Article Search Wrapper
=============================

Unofficial Python wrapper for the NY Times Article Search API.

API docs: http://developer.nytimes.com/docs/read/article_search_api_v2

Example usage:

```python
articlesearch = ArticleSearch()
articlesearch.search_terms("new+york+times")
articlesearch.set_return_fields("snippet,lead_paragraph")
articlesearch.make_request()
decoded_response = articlesearch.get_decoded_response()
print decoded_response["response"]["docs"][1]
```