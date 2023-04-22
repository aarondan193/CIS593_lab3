from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import pymongo
from pymongo import MongoClient
import json
#consumer key, consumer secret, access token, access secret.
consumer_key = "Qsr8LCv7y6lAAA00CM2mW9YBs"
consumer_secret = "Wcj7t8AHBHd2axYL8igac8aeMluJrOGmrdwo5BsxAWthsxFYQx"
access_token = "1501730203369881601-4OfpHxyHIDmr7n7GGa3RjrcZzN3OU7"
access_token_secret = "A7RCbahzcNH8gRS2yLNWRLouOfWkMUcRecV32lsMt1dUU"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAO89aAEAAAAA6nM52Ef43%2FY3feUSkY9CP0SrvSE%3DvRihqNeeiC8p4KSZRihedeJYjYv3g2bmJBQZgd99b82NTXez8K"
# The MongoDB connection info.
conn = MongoClient('localhost', 27017)
# This assumes your database name is ElectionDataStream.
db = conn.ElectionDataStream
# Your collection name is tweets.
collection = db.tweets
db.tweets.create_index([("id", pymongo.ASCENDING)],unique = True,)
class getStreamData(StreamListener):
    def on_data(self, data):
    # Load the Tweet into the variable "tweet"
        try:
            tweet = json.loads(data)
            # Pull important data from the tweet to store in the database
            #One at a time.
            collection.insert_one(tweet)
            return True
        except:
            pass

if __name__ == "__main__":
 authentication = OAuthHandler(consumer_key, consumer_secret)
 authentication.set_access_token(access_token, access_token_secret)
 tweetStream = Stream(authentication, getStreamData())
 # Here write down your keywords which you want to search for.
 tweetStream.filter(track=["Corona","Trump","Trunp Tested Positive"],languages=['en']) 
