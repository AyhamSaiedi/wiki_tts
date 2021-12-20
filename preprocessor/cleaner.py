import re


def unpack_tuple_into_list(query_content):
    """ In order to decode our byte data types into strings, it is here necessary to unpack
    the elements out of tuples_list and assign them to input_text.
    First, we're initializing a new list and will leave it empty:

    :param query_content: returned value of the SQL query
    """

    input_text = []
    for articles_tuple in query_content:
        for bytes_elements in articles_tuple:
            decoded = bytes_elements.decode()
            input_text.append(decoded)

    return input_text

def clean(input_text):
    """ Regex operations for text transformation. """

    # substituting with ''
    expressions_without_whitespace = {
        'datei_meta': r'(^.*Datei.*$)',
        'bild_meta': r'(^.*Bild.*$)',
        #'kategorie_meta': r'(^.*Kategorie.*$)',
        'all_brackets': r'([\[\]])|([\(\)])|([\{\}])',
        'reveal_title': r'(([\']{2}))',
        'http_links': r'(http\S+)',
        'asterix': r'\*',
        'strike_through': r'~',
        'table_1': r':-',
    }

    # substituting with ' '
    expressions_with_whitespace = {
        #'replace_newline_with_space': r'\n+',
        'table_2': r'\|',
        'hashtags': r'#',
        #'double_newline': r'\s\s+'
    }

    wo_whitespace_joined = '|'.join(expressions_without_whitespace.values())
    text = re.sub(wo_whitespace_joined, '', input_text, 0, re.MULTILINE)
    
    w_whitespace_joined = '|'.join(expressions_with_whitespace.values())
    text = re.sub(w_whitespace_joined, ' ', text, 0, re.MULTILINE)

    text_transformed = text.strip()
    return text_transformed

def abbreviation_extender(input_text):
    """ Regex operations for text transformation. """

    # substituting with ''
    abbreviations_german = {
        'Abbildung': r'Abb\.',
        'Abkürzung': r'Abk\.',
        'allgemein': r'allg\.',
        'besonders': r'bes\.',
        'eigentlich': r'eigtl\.',
        'geboren': r'geb\.',
        'jemand': r'jmd\.',
        'jemandem': r'jmdm\.',
        'jemanden': r'jmdn\.',
        'oder Ähnliches': r'o\. Ä\.',
        'und': r'u\.',
        'unter Anderem': r'u\.a\.',
        'und so weiter': r'usw\.',
        'beziehungsweise': r'bzw\.',
        'bezüglich': r'bzgl\.'
    }

    # abb_joined_1 = '|'.join(abbreviations_german.values())
    # abb_joined_2 = '|'.join(abbreviations_german.keys())
    
    for key, value in abbreviations_german.items():
        text = re.sub(value, key, input_text, 0, re.IGNORECASE | re.MULTILINE)

    return text
        
        
    


tt = """
Datei:Möckenlohe Pfarrkirche von NO.jpg|miniatur|Pfarrkirche von Möckenlohe
Die '''Wehrkirche Möckenlohe''' ist Abb. eine#teilweise abk. erhaltene Wehrkirche, 

Wallfahrtskirche und katholische ''Pfarrkirche Mariä Himmelfahrt'' in Möckenlohe, einem Gemeindeteil von Adelschlag im Landkreis Eichstätt im Naturpark Altmühltal Bayern.
"""

# ss = clean(tt)

# pp = abbreviation_extender(ss)

# print(pp)