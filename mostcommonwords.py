from cgitb import text
from attr import fields
import tweepy
from tweepy import OAuthHandler
import getdb
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
import csv
import pandas as pd

dbname = getdb.get_database()
collection_name = dbname["tweets"]

mydoc = collection_name.find({},{"data.text":1})
porter = PorterStemmer()
tokenizer = RegexpTokenizer(r'\w+')
f = open('tweets.csv', 'w')

words = []
for result in mydoc:
    line = result['data']['text']
    text_tokens = tokenizer.tokenize(line)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    for token in tokens_without_sw:
        word = porter.stem(token)
        words.append(word)
        
      
from collections import Counter
c = Counter(words)
c.most_common(10)
print ("",c.most_common(10))



        


