from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import Q
from requests.api import request

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


client = Elasticsearch()
s1 = Search(using=client)
s2 = Search(using=client)
s3 = Search(using=client)
## QUERY-1 :To list all books having either Android or Practice in titles and having less than 500 pages
# Increasing the score of books having Action or Unlocking in there titles

q = Q('bool', must=[Q('match', title='Android Practice')],should=[Q('match', title='Action'),Q('match', title='Unlocking')],must_not=[Q('range',pageCount={'gte':500})])
s1= s1.query(q)
response = s1.execute()

for hit in s1:
    print hit.title

print "--------"

## QUERY-2 :To list all books having either Android or Practice in titles and having less than 500 pages
# Only keeping the books who have atleast Action or Unlocking in there title.
q = Q('bool',minimum_should_match=1,must=[Q('match', title='Android Practice')],should=[Q('match', title='Action'),Q('match', title='Unlocking')],must_not=[Q('range',pageCount={'gte':500})])
s2= s2.query(q)
response = s2.execute()

for hit in s2:
    print hit.title

print "--------"
## QUERY-2 :To exhibit boosting in terms of positive and negative effect.
# Increasing the scores of books which match Data and decreasing score by factor of 0.5 where title is 'Validating Data with Validator'.
q = Q('boosting', positive=Q('match',title='Data'),negative=Q('match',title='Validating Data with Validator'),negative_boost=0.5)
s3= s3.query(q)
response = s3.execute()

for hit in s3:
    print hit.title

