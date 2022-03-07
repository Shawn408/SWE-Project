import requests


def wiki_link_search(keyword):
    BASE_URL = "https://en.wikipedia.org/w/api.php"
    params = {
        "action" : "query",
        "prop" : "info",
        "inprop" : "url",
        "titles": keyword,
        "format": "json",
        "formatversion": "2",
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()
    title_search = data['query']['pages'][0]['fullurl']
    return title_search


