import re


def find_title(text):
    """ Searches for and returns the title of the article within a text body that has already been normalized.
    The title is defined as the text that exists between two single-quatation marks ('').
    This has proved to be consistent throughout the wikipedia markdown syntax. Will fail in case of different (foreign) input syntax.

    :param text: takes in the normalized text as input
    """

    if(text := re.search(r'([\']{1})(?:(?=(\\?))\2.)*?\1', text, re.MULTILINE)) is not None:
        title = text.group()

        ### .strip() NOT WORKING !!! ###
        title = title.strip()
        return title
    else:
        return None

def find_subheader(text):
    """ Searches for and returns the subheaders from a Wikipedia-text that has already been normalized.
    The title is defined as the text that exists between equal signs (=).
    This has proved to be consistent throughout the wikipedia markdown syntax. Will fail in case of different (foreign) input syntax.

    :param text: takes in the normalized text as input
    """

    if(text := re.findall(r'\={2}.*?\={2}', text, re.MULTILINE)) is not None:
        return text
    else:
        return None


def clean_subheaders(subheaders):
    """ Cleans the extracted subheaders from the symbols that accompany them

    :param subheaders: takes in subheaders of the Wikipedia markdown syntax
    """
    cleaned_subheaders = []
    for i in subheaders:
        cleaned_subheaders.append(
            list(map(lambda s: s.strip('=').strip(' '), i)))
    return cleaned_subheaders


# New function. Work in progress...
def find_ns_coordinates(text):

    if(found := re.search(r'(NS|n|s)(=)([0-9]|[0-9][0-9])(\.)([0-9][0-9][0-9][0-9][0-9][0-9]|[0-9][0-9][0-9][0-9][0-9]|[0-9][0-9][0-9][0-9]|[0-9][0-9][0-9]|[0-9][0-9]|[0-9])', text, re.MULTILINE)) is not None:
        text = found
        ns_coordinates = text.group()
        return ns_coordinates.strip('NS=')
        
    elif(found := re.search(r'(Breitengrad) (=) ([0-9]|[0-9][0-9])(\.)([0-9][0-9][0-9][0-9][0-9][0-9]|[0-9][0-9][0-9][0-9][0-9]|[0-9][0-9][0-9][0-9]|[0-9][0-9][0-9]|[0-9][0-9]|[0-9])', text, re.MULTILINE)):
        text = found
        b_coordinates = text.group()
        return b_coordinates.strip('Breitengrad = ')
    else:
        return None


def find_ew_coordinates(text):

    if(found := re.search(r'(EW|e|w)(=)([0-9]|[0-9][0-9])(\.)([0-9][0-9][0-9][0-9][0-9][0-9]|[0-9][0-9][0-9][0-9][0-9]|[0-9][0-9][0-9][0-9]|[0-9][0-9][0-9]|[0-9][0-9]|[0-9])', text, re.MULTILINE)) is not None:
        text = found
        ew_coordinates = text.group()
        return ew_coordinates.strip('EW=')

    elif(found := re.search(r'(Längengrad) (=) ([0-9]|[0-9][0-9])(\.)([0-9][0-9][0-9][0-9][0-9][0-9]|[0-9][0-9][0-9][0-9][0-9]|[0-9][0-9][0-9][0-9]|[0-9][0-9][0-9]|[0-9][0-9]|[0-9])', text, re.MULTILINE)) is not None:
        text = found
        l_coordinates = text.group()
        return l_coordinates.strip('Längengrad = ')
    else:
        return None
    
def category_finder(text):

    if(text := re.findall(r'(^.*Kategorie.*$)', text, re.MULTILINE)) is not None:
        text = [i.strip("Kategorie:") for i in text]
        print(text)
        return text
    else:
        return None

# tt = """Navigationsleiste Wehrkirchen im Landkreis Eichstätt

# Coordinate|NS=48.822269|EW=11.226129|type=landmark|region=DE-BY
# """
# n = find_ns_coordinates(tt)
# e = find_ew_coordinates(tt)

# print(n, e)

# tex = """

# Navigationsleiste Burgen und Schlösser im Landkreis Kitzingen

# Kategorie:Niederungsburg in Unterfranken Rimbach
# Kategorie:Bauwerk in Volkach
# Kategorie:Bodendenkmal in Volkach
# Kategorie:Abgegangenes Bauwerk im Landkreis Kitzingen
# Kategorie:Burg in Europa Rimbach
# Kategorie:Burg im Landkreis Kitzingen Rimbach"""
