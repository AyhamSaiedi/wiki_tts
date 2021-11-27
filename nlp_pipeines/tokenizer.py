import spacy
from spacy.matcher import Matcher
from spacy import displacy

nlp = spacy.load("de_dep_news_trf")

matcher = Matcher(nlp.vocab)

pattern = [{"TEXT": "ns"}, {"IS_DIGIT": True}]
matcher.add("MARIA_KIRCHEN", [pattern])



doc = nlp('''
die römisch-katholische filialkirche 'mariä geburt' ist die dorfkirche von 
untereschenbach hammelburg untereschenbach, einem stadtteil von hammelburg im landkreis bad kissingen.
coordinate ns=50.11523 ew=9.8608
die kirche besteht aus dem langhaus kirche langhaus und dem zweigeschossigen chor architektur chor im osten. 
''')

options = {"compact": True, "color": "blue", "fine_grained": True}
displacy.serve(doc, style="dep", options=options)

# for token in doc:
#     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#             token.shape_, token.is_alpha, token.is_stop)

# matches = matcher(doc)

# for match_id, start, end in matches:
#     matched_span = doc[start:end]
#     print(matched_span.text)
