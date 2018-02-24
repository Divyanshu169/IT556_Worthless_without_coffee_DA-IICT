import spacy
from elasticsearch import Elasticsearch
from pprint import pprint
import json
import requests

#es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
nlp = spacy.load('en')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')

"""
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
"""
data = json.load(open('json_book.json'))

for i in data["books"]:
    print (i)
    print("\n-----------------------\n")
    #es.index(index='book2', doc_type='book_doc', id=i['title'], body=i)
    doc=nlp(i['title'])
    #print (list(doc.noun_chunks))
