from operator import eq
from attr import fields
import tweepy
from tweepy import OAuthHandler
import getdb
import json
import pandas

bearer_token  = "AAAAAAAAAAAAAAAAAAAAAO89aAEAAAAA6nM52Ef43%2FY3feUSkY9CP0SrvSE%3DvRihqNeeiC8p4KSZRihedeJYjYv3g2bmJBQZgd99b82NTXez8K"

query = 'Covid'
dbname = getdb.get_database()
collection_name = dbname["tweets"]

class IDPrinter(tweepy.StreamingClient):
    def on_data(self, raw_data):
        data = json.loads(raw_data)
        collection_name.insert_one(data)
        return super().on_data(raw_data)


        
printer = IDPrinter(bearer_token)

#print(str(printer.get_rules()))
#printer.delete_rules(ids=[1504155908783362048])
#printer.add_rules("add",{"value": "Covid","tag": "Covid"})

printer.filter(expansions=['author_id','referenced_tweets.id','referenced_tweets.id.author_id','entities.mentions.username','attachments.poll_ids','attachments.media_keys','in_reply_to_user_id','geo.place_id'], 
    tweet_fields=['context_annotations','created_at','author_id','source','attachments','public_metrics','conversation_id','entities','geo','id','in_reply_to_user_id','lang','possibly_sensitive','referenced_tweets','reply_settings','text','withheld'],
    place_fields=['place_type','country','country_code','full_name','geo','id','name','contained_within'],
    user_fields=['created_at','description','entities','id','location','name','pinned_tweet_id','profile_image_url','protected','public_metrics','url','username','verified','withheld'])

   

