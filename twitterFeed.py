import tweepy

API_KEY = "YOUR_KEY"
API_SECRET = "YOUR_SECRET"
ACCESS_TOKEN = "YOUR_TOKEN"
ACCESS_SECRET = "YOUR_ACCESS_SECRET"

# Setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api

def get_link_from_object(tweet):
    return "https://twitter.com/"+tweet.user.screen_name+"/status/"+str(tweet.id)

# Create API object
api = connect_to_twitter_OAuth()