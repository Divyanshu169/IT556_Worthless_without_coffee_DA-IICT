from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from requests.api import request

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


client = Elasticsearch()

## QUERY-1 : to list all books of a particular author.

s = Search(using=client, index="book_self") \
    .query("match",  author = "Benjamin Pollack")
response = s.execute()

print('Number of books by author %s: %d' %("Benjamin Pollack",response.hits.total))
for hit in s:
    print(' Name: %s, Publisher: %s, Genre: %s, Synopsis: %s' % (hit.name, hit.publisher, hit.genre, hit.synopsis))

## QUERY-2 : Genre.

s = Search(using=client, index="book_self") \
    .query("match",  genre = "elasticsearch")
response = s.execute()

print('\n Number of books belonging to genre %s: %d' % ("elasticsearch", response.hits.total))
for hit in s:
    print('Name: %s, Author: %s, Publisher: %s, Synopsis: %s' %(hit.name, hit.author, hit.publisher, hit. synopsis))

## QUERY-3 : Book.

s = Search(using=client, index="book_self") \
    .query("match",  name= "abcd") \

response = s.execute()

for hit in s:
    print('\n Name: %s, Author: %s, Publisher: %s, Genre: %s, Synopsis: %s' %(hit.name, hit.author, hit.publisher, hit.genre, hit. synopsis))





