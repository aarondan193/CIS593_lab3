from attr import fields
import tweepy
from tweepy import OAuthHandler
import getdb

CONSUMER_KEY= "Qsr8LCv7y6lAAA00CM2mW9YBs"
CONSUMER_SECRET="Wcj7t8AHBHd2axYL8igac8aeMluJrOGmrdwo5BsxAWthsxFYQx"
OAUTH_TOKEN="1501730203369881601-4OfpHxyHIDmr7n7GGa3RjrcZzN3OU7"
OAUTH_TOKEN_SECRET="A7RCbahzcNH8gRS2yLNWRLouOfWkMUcRecV32lsMt1dUU"
bearer_token  = "AAAAAAAAAAAAAAAAAAAAAO89aAEAAAAA6nM52Ef43%2FY3feUSkY9CP0SrvSE%3DvRihqNeeiC8p4KSZRihedeJYjYv3g2bmJBQZgd99b82NTXez8K"

query = 'niagara  -is:retweet'

#stream = tweepy.Stream(
#    CONSUMER_KEY, CONSUMER_SECRET,
#    OAUTH_TOKEN, OAUTH_TOKEN_SECRET
#)

dbname = getdb.get_database()
collection_name = dbname["tweets"]

client = tweepy.Client(bearer_token=bearer_token)
response = client.search_recent_tweets(query=query, expansions=['author_id','referenced_tweets.id','referenced_tweets.id.author_id','entities.mentions.username','attachments.poll_ids','attachments.media_keys','in_reply_to_user_id','geo.place_id'], 
    tweet_fields=['context_annotations','created_at','author_id','source','attachments','public_metrics','conversation_id','entities','geo','id','in_reply_to_user_id','lang','possibly_sensitive','referenced_tweets','reply_settings','text','withheld'],
    place_fields=['contained_within','country','country_code','full_name','geo','id','name','place_type'],
    user_fields=['created_at','description','entities','id','location','name','pinned_tweet_id','profile_image_url','protected','public_metrics','url','username','verified','withheld'])

#print (type(response))
#print (dir(response))
print (response.data)
print()
print (response.includes)
print()
print (response.errors)
print()
print (response.meta)
print()
for tweet in response.data:
    #print (str(response.includes))
    collection_name.insert_one(tweet.data)
    
    