import requests
import json


def wiki_appropriate_title(title):

    if title is None:
        return None

    title = title.replace(" ", "_")
    title = title.strip("\n'")

    ##     Getting title ID through Mediawiki's API (GET PAGE API)     ###

    url = 'https://de.wikipedia.org/w/rest.php/v1/page/' + title + '/bare'
    headers = {'User-Agent': 'MediaWiki REST API docs examples/0.1 (https://www.mediawiki.org/wiki/API_talk:REST_API)'}

    response = requests.get(url, headers=headers)

    if response.ok:
        return title

    elif not response.ok:

        search_query = title
        number_of_results = 5
        url = 'https://de.wikipedia.org/w/rest.php/v1/search/title'
        headers = {'User-Agent': 'MediaWiki REST API docs examples/0.1 (https://www.mediawiki.org/wiki/API_talk:REST_API)'}

        response = requests.get(url, headers=headers, params={'q': search_query, 'limit': number_of_results})
        data = response.json()

        if response.ok:
            data = response.json()
            for item in data['pages']:
                return item['key']
        else:
            return None
    else:
        return None

# s = wiki_appropriate_title('Deutsches_Freimaurer-Museum')
# print(s)
