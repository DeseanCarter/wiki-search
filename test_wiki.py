import requests
from flask import Flask, jsonify
app = Flask(__name__)

#value = input("Please input a subject to get response from Wikipedia")

#GET request
@app.route('/')
def hello_world():
    payload = {
    "action": "query",
    "format": "json",
    "titles": "dog",
    "prop": "info|iwlinks",
    "limit": 500,
    "iwprop": "url",
    }
    search_results = requests.get('http://en.wikipedia.org/w/api.php?', params= payload)
    search_results.status_code
    DATA =  search_results.json()
    PAGES = DATA["query"]["pages"]
    return PAGES
    import pdb; pdb.set_trace()
    
#POST requests
@app.route('/dog')
def new_world():
    payload = {'key1': 'value1'}
    search_results2 = requests.post('https://www.mediawiki.org/wiki/API:Search/', data= payload)
    # import pdb; pdb.set_trace()
    return 'Hello New World'


@app.route('/ordinary')
def evil_world():
    payload = {'key1': 'value1'}
    search_results = requests.post('https://www.mediawiki.org/wiki/API:Search', params= payload)
    # import pdb; pdb.set_trace()
    return 'evil World'    


if __name__ == '__main__':
    # run app in debug mode
    app.run(debug=True)    