'''import requests
res = requests.get('http://localhost:9200')
print(res.content)'''

from elasticsearch import Elasticsearch
from pprint import pprint
import json
import requests
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

'''PUT book2
{
  "settings": {
    "analysis": {
      "filter": {
                "my_stop": {
                    "type":       "stop",
                    "stopwords":  "_english_"
                }
            },
      "analyzer": {
        "title_analyzer": {
          "type":      "custom",
          "tokenizer": "pattern",
          "filter": [
            "lowercase",
            "my_stop"
          ]
        }
      }
    }
  },
  "mappings": {
    "book_doc": { 
      "properties": { 
        "id" : { "type": "integer" },
        "title":    { "type": "text",
                      "analyzer": "title_analyzer"
                    }, 
        "isbn" : { "type": "keyword"},
        "pageCount" : { "type": "integer"},
        "publishedDate" : { "type": "date"},
        "thumbnailUrl" : { "type": "text"},
        "shortDescription" : { "type": "text"  }, 
        "longDescription" : { "type": "text"  }, 
        "status":     { "type": "keyword"  }, 
        "authors" : { "type": "text"  }, 
        "categories":      { "type": "keyword" }
      }
    }
  }
}'''

data = json.load(open('json_book.json'))

for i in data["books"]:
	print i
	es.index(index='book2', doc_type='book_doc', id=i['id'], body=i)


