import urllib.request
import sys
import json
from wordSimilarity import *

word1 = input(" Enter the word1 : ")
word2 = input(" Enter the word2 : ")


#url = "http://spotlight.dbpedia.org/rest/annotate?types=DBPedia:Person&text="+sentence+"&confidence=0.2&support=20"
url = "http://ws4jdemo.appspot.com/ws4j?measure=wup&args="+word1+"%3A%3A"+word2
#print(url)
request = urllib.request.Request(url)
request.add_header('Accept', 'application/json')
response = urllib.request.urlopen(request)

responseStr = response.read().decode('utf-8')

# fetch json from the response
jsonStr = json.loads(responseStr)

print(jsonStr['result'][0]['score'])
