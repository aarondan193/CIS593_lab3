import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY= "Qsr8LCv7y6lAAA00CM2mW9YBs"
CONSUMER_SECRET="Wcj7t8AHBHd2axYL8igac8aeMluJrOGmrdwo5BsxAWthsxFYQx"
OAUTH_TOKEN="1501730203369881601-4OfpHxyHIDmr7n7GGa3RjrcZzN3OU7"
OAUTH_TOKEN_SECRET="A7RCbahzcNH8gRS2yLNWRLouOfWkMUcRecV32lsMt1dUU"


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

