import json
import requests
from elasticsearch import Elasticsearch

#JSON files
filename = 'product_info_LA1_test.json'

# use ES default connection
es = Elasticsearch()
r  = requests.get('http://localhost:9200')

#insert document
def insert_doc(doc):
  global i
  es.index(index='la1_test', id=i, body=doc)
  print('insert %s document' % i)
  i += 1


#Create _id
i = 1
if (r.status_code  == 200):
  #load data
  with open(filename) as f:
    data = f.read()
  
  docs = json.loads(data)
  for doc in docs:
    if(doc['specifications']=='NA'):
      doc['specifications']={}
      insert_doc(doc)
    else:
      insert_doc(doc)
