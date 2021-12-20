import requests

###     Revision object     ###


def find_if_minor(title):

    if title is None:
        return None

    url = 'https://de.wikipedia.org/w/rest.php/v1/page/' + title + '/history'
    headers = {'User-Agent': 'MediaWiki REST API docs examples/0.1 (https://www.mediawiki.org/wiki/API_talk:REST_API)'}

    response = requests.get(url, headers=headers)

    if response.ok:
        data = response.json()
        revisions = data['revisions']

        # if there were three or more return max !!!!!!!!!!!!!!!!!!
        latest_revisions=revisions[0:3]

        data_list=[]
        for revision in latest_revisions:
            is_minor=revision['minor']
            timestamp=revision['timestamp']
            data_tuple=(timestamp, is_minor)
            data_list.append(data_tuple)
        return data_list
    else:
        return None


# page=find_if_minor('Turmhügel_Altcastell')
# print(page)
