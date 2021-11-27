import re
import fileinput
import itertools
from itertools import cycle
from typing import Iterable
import pandas as pd
from functools import partial

headers = [['history', 'mistery'], ['consider', 'required']]
text = [' history this right here is something to test our data with it has got a and mistery that will interest you',
        'consider this is also interesting what do you better though you have to find out soon you are required to do so, so tell me please']


def paragrapher(input_iterable, input_text):

    def pairwise(input_iterable):
        a, b = itertools.tee(input_iterable)
        next(b, None)
        return zip(a, b)

    s = pairwise(input_iterable)
    l = list(s)
    # print(l)

    new = [list(a) for a in l]
    new_new = []
    for x, y in new:
        from_to = x + r'(.*?)' + y
        regex = re.findall(from_to, input_text, re.MULTILINE | re.DOTALL)
        new_new.append(regex)

    return new_new

# Merging and applying DataFrame.
# article = {
#     'text': text,
#     'headers': headers,
# }

# pd.set_option("display.max_rows", None, "display.max_columns", None)
# pd.set_option('display.max_colwidth', None)

# pdf = pd.DataFrame(article)

# pdf['col_3'] = pdf.apply(lambda x: paragrapher(x.headers, x.text), axis=1)
