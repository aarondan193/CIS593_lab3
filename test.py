import pymongo
from pymongo import MongoClient
import json
import twitter
from pprint import pprint

CONSUMER_KEY = "Qsr8LCv7y6lAAA00CM2mW9YBs"
CONSUMER_SECRET ="Wcj7t8AHBHd2axYL8igac8aeMluJrOGmrdwo5BsxAWthsxFYQx"
OAUTH_TOKEN = "1501730203369881601-4OfpHxyHIDmr7n7GGa3RjrcZzN3OU7"
OAUTH_TOKEN_SECRET = "A7RCbahzcNH8gRS2yLNWRLouOfWkMUcRecV32lsMt1dUU"
bearer_token  = "AAAAAAAAAAAAAAAAAAAAAO89aAEAAAAA6nM52Ef43%2FY3feUSkY9CP0SrvSE%3DvRihqNeeiC8p4KSZRihedeJYjYv3g2bmJBQZgd99b82NTXez8K"

auth=twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
twitter_api=twitter.Twitter(auth=auth)



client=MongoClient()
db=client.tweet_db
tweet_collection=db.tweet_collection
tweet_collection.create_index([("id",pymongo.ASCENDING)],unique=True)


count=50
q="Salesforce"
search_results=twitter_api.search.tweets(count=count,q=q)
#pprint(search_results['search_metadata'])


statuses=search_results["statuses"]

since_id_new=statuses[-1]['id']

for statues in statuses:
       try:
              tweet_collection.insert(statues)
       except:
              pass
       
       
tweet_cursor=tweet_collection.find()
print(tweet_cursor.count())
user_cursor=tweet_collection.distinct("user.id")
print(len(user_cursor))

for document in tweet_cursor:
       try:
              print('-----')
              print('name:-',document["user"]["name"])
              print('text:-',document["text"])
              print('Created Date:-',document["created_at"])
       except:
              print("Error in Encoding")
              pass