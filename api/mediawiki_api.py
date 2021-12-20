# Title matching
# Get page ID (get page source, get page object)
# Get page history
# Compare revisions
# Maybe get languages


import requests
import json

# GET PAGE:

def get_id(title):

    if title is None:
        return None

    title = title.replace(" ", "_")
    title = title.strip("\n'")

###     Getting title ID through Mediawiki's API (GET PAGE API)     ###

    url = 'https://de.wikipedia.org/w/rest.php/v1/page/' + title + '/bare'
    headers = {'User-Agent': 'MediaWiki REST API docs examples/0.1 (https://www.mediawiki.org/wiki/API_talk:REST_API)'}

    response = requests.get(url, headers=headers)

    if response.ok:

        data = response.json()
        return data['id']

###     Getting ID after putting the title through Mediawiki's auto complete API (AUTO COMPLETE API)     ###

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
                return item['id']
        else:
            return None
    else:
        return None

    





# search_query = 'Deutsche_Freimaurer-Museum'
# number_of_results = 3
# endpoint = 'search/page'
# base_url = 'https://de.wikipedia.org/w/rest.php/v1/'

# headers = {'User-Agent': 'MediaWiki REST API docs examples/0.1 (https://meta.wikimedia.org/wiki/User:APaskulin_(WMF))'}

# url = base_url + endpoint
# response = requests.get(url, headers=headers, params={'q': search_query, 'limit': number_of_results})
# response = json.loads(response.text)

# for page in response['pages']:
#   print(page['title'])