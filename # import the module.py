# import the module
import tweepy

# assign the values accordingly
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# assign the values accordingly
consumer_key = "Qsr8LCv7y6lAAA00CM2mW9YBs"
consumer_secret = "Wcj7t8AHBHd2axYL8igac8aeMluJrOGmrdwo5BsxAWthsxFYQx"
access_token = "1501730203369881601-4OfpHxyHIDmr7n7GGa3RjrcZzN3OU7"
access_token_secret = "A7RCbahzcNH8gRS2yLNWRLouOfWkMUcRecV32lsMt1dUU"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAO89aAEAAAAA6nM52Ef43%2FY3feUSkY9CP0SrvSE%3DvRihqNeeiC8p4KSZRihedeJYjYv3g2bmJBQZgd99b82NTXez8K"

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

# the screen name of the user
screen_name = "geeksforgeeks"

# fetching the user
user = api.get_user(screen_name)

# printing the information
print("The id is : " + str(user.id))
print("The id_str is : " + user.id_str)
print("The name is : " + user.name)
print("The screen_name is : " + user.screen_name)
print("The location is : " + str(user.location))
print("The profile_location is : " + str(user.profile_location))
print("The description is : " + user.description)


print("The url is : " + user.url)
print("The entities are : " + str(user.entities))
print("Is the account protected? : " + str(user.protected))

print("The followers_count is : " + str(user.followers_count))
print("The friends_count is : " + str(user.friends_count))
print("The listed_count is : " + str(user.listed_count))
print("The account was created on : " + str(user.created_at))
print("The favourites_count is : " + str(user.favourites_count))
print("The utc_offset is : " + str(user.utc_offset))
print("The geo_enabled is : " + str(user.geo_enabled))
print("The verified is : " + str(user.verified))
print("The statuses_count is : " + str(user.statuses_count))
print("The lang is : " + str(user.lang))
print("The status ID is : " + str(user.status.id))
print("The contributors_enabled is : " + str(user.contributors_enabled))
print("The is_translator is : " + str(user.is_translator))
print("The is_translation_enabled is : " + str(user.is_translation_enabled))

print("The profile_background_color is : " + user.profile_background_color)
print("The profile_background_image_url is : " + user.profile_background_image_url)
print("The profile_background_image_url_https is : " + user.profile_background_image_url_https)
print("The profile_background_tile is : " + str(user.profile_background_tile))
print("The profile_image_url is : " + user.profile_image_url)
print("The profile_image_url_https is : " + user.profile_image_url_https)
print("The profile_banner_url is : " + user.profile_banner_url)
print("The profile_link_color is : " + user.profile_link_color)
print("The profile_sidebar_border_color is : " + user.profile_sidebar_border_color)
print("The profile_sidebar_fill_color is : " + user.profile_sidebar_fill_color)
print("The profile_text_color is : " + user.profile_text_color)
print("The profile_use_background_image is : " + str(user.profile_use_background_image))

print("The has_extended_profile is : " + str(user.has_extended_profile))
print("The default_profile is : " + str(user.default_profile))
print("The default_profile_image is : " + str(user.default_profile_image))
print("Is the authenticated user following the account? : " + str(user.following))

print("Has the authenticated user requested to follow the account? : " + str(user.follow_request_sent))
print("Are notifications of the authenticated user turned on for the account? : " + str(user.notifications))
