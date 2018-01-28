'''import requests
res = requests.get('http://localhost:9200')
print(res.content)'''

from elasticsearch import Elasticsearch
from pprint import pprint
import json
import requests
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
"""this shows the mapping"""
request_body = {
	    "settings" : {
	        "number_of_shards": 5,
	        "number_of_replicas": 1
	    },

	    'mappings': {
	        'book_doc': {
	            'properties': {
					'id': {'type':'int'},
	                'name': {'type': 'text'},
	                'author': {'type': 'text'},
	                'publisher': {'type': 'text'},
	                'genre': {'type': 'text'},
	                'synopsis': {'type': 'text'},
	            }}}
	}

data = json.load(open('data1.json'))

for i in data['books']:
	es.index(index='book_self', doc_type='book_doc', id=i['id'], body=i)
	print i

