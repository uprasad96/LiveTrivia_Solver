from googlesearch.googlesearch import GoogleSearch
response = GoogleSearch().search("State dance assam")
for result in response.results:
    print("Title: " + result.title)
    print("Content: " + result.getText())
