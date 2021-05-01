import requests
from flask import Flask, jsonify
app = Flask(__name__)

API = ''
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

    links = []
    new_dict = {"links":links}

    for key, value in PAGES.items():
        print(key)

    singleurl = PAGES[key]["iwlinks"]

    singleurl2 = PAGES[key]["iwlinks"][0]["url"]
    
    print(singleurl2)

    # length of point in dict
    print(len(PAGES[key]))
    
    
    for x in singleurl:
        links.append(x["url"])
        

    print(new_dict)

    import json
    return jsonify(new_dict)
    import pdb; pdb.set_trace()

    
if __name__ == '__main__':
    # run app in debug mode
    app.config['SERVER_NAME'] = 'wiki-search.com:5000'
    app.run(debug=True)
