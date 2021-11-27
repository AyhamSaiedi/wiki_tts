""" importing regex """
import re


def clean_old(text, datei_meta=True,
        kategorie_meta=True, brackets=True,
        q_title=True, http_link=True,
        newline=True, quote=True,
        bullet_point=True, link=True,
        strikethrough=True, spoiler=True,
        code=True, superscript=True,
        table=True, heading=True):

    # Remove lines that have meta information relating to Data type. Keyword: Datei
    if datei_meta:
        text = re.sub(r'(^.*Datei.*$)', '', text, 0, re.MULTILINE)

    # Remove lines that have meta information relating to Category. Keyword: Kategorie
    if kategorie_meta:
        text = re.sub(r'(^.*Kategorie.*$)', '', text, 0, re.MULTILINE)

    # Remove all kinds of brackets
    if brackets:
        text = re.sub(r'([\[\]])|([\(\)])|([\{\}])', '', text, 0, re.MULTILINE)

    # Remove quotation marks to reveal title
    if q_title:
        text = re.sub(r'(([\']{2}))', '', text, 0, re.MULTILINE)

    # Remove http links
    if http_link:
        text = re.sub(r'(http\S+)', '', text, 0, re.MULTILINE)

    # Newlines (replaced with space to preserve cases like word1\nword2)
    if newline:
        text = re.sub(r'\n+', ' ', text)

        # Remove resulting ' '
        text = text.strip()
        text = re.sub(r'\s\s+', ' ', text)

    # > Quotes
    if quote:
        text = re.sub(r'\"?\\?&?gt;?', '', text)

    # Bullet points/asterisk (bold/italic)
    if bullet_point:
        text = re.sub(r'\*', '', text)
        text = re.sub('&amp;#x200B;', '', text)

    if link:
        text = re.sub(r'\[.*?\]\(.*?\)', '', text)

    # Strikethrough
    if strikethrough:
        text = re.sub('~', '', text)

    # Spoiler, which is used with < less-than (Preserves the text)
    if spoiler:
        text = re.sub('&lt;', '', text)
        text = re.sub(r'!(.*?)!', r'\1', text)

    # Code, inline and block
    if code:
        text = re.sub('`', '', text)

    # Superscript (Preserves the text)
    if superscript:
        text = re.sub(r'\^\((.*?)\)', r'\1', text)

    # Table
    if table:
        text = re.sub(r'\|', ' ', text)
        text = re.sub(':-', '', text)

    # Heading
    if heading:
        text = re.sub('#', '', text)

    text = text.lower()
    return text
