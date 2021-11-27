import re

abbreviations_german = {
    'Abbildung': r'/^Abb\.$/',
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

text_input = 'eine abb. und auch andere sachen'

for key, value in abbreviations_german.items():
    j = '|'.join(value)
    if re.match(j, text_input):
        text = re.sub(j, key, text_input, 0, re.IGNORECASE | re.MULTILINE)

print(text)

