# import the module
import requests
import os
import json
import tweepy

# assign the values accordingly
consumer_key = "Qsr8LCv7y6lAAA00CM2mW9YBs"
consumer_secret = "Wcj7t8AHBHd2axYL8igac8aeMluJrOGmrdwo5BsxAWthsxFYQx"
access_token = "1501730203369881601-4OfpHxyHIDmr7n7GGa3RjrcZzN3OU7"
access_token_secret = "A7RCbahzcNH8gRS2yLNWRLouOfWkMUcRecV32lsMt1dUU"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAO89aAEAAAAA6nM52Ef43%2FY3feUSkY9CP0SrvSE%3DvRihqNeeiC8p4KSZRihedeJYjYv3g2bmJBQZgd99b82NTXez8K"


client = tweepy.Client(bearer_token=bearer_token)

query = 'Ukraine'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations','created_at','author_id','source','attachments','public_metrics','conversation_id','entities','geo','id','in_reply_to_user_id','lang','possibly_sensitive','referenced_tweets','reply_settings','text','withheld'],
                                     user_fields=['created_at,public_metrics,name'],expansions=['author_id','referenced_tweets.id','referenced_tweets.id.author_id','entities.mentions.username','attachments.poll_ids','attachments.media_keys','in_reply_to_user_id','geo.place_id'], max_results=10)

for tweet in tweets:
    print(type(tweet))
    print (tweet)


#json.dumps(tweets.data,separators=(','))



# Get users list from the includes object
#users = {u["id"]: u for u in tweets.includes['users']}

for tweet in tweets:
    #print (dir(tweet))
    print (str(tweet.includes) + "\n")
    #if tweet.geo.place_type:
    #    print(tweet.geo.place_type)
    #if tweet.author_id:
    #    print(tweet.author_id)
        