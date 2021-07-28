#libraries used
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

#api and access keys from twitter
API_KEY = os.environ.get("API_KEY")
API_KEY_SECRET = os.environ.get("API_KEY_SECRET")
ACCESS_KEY = os.environ.get("ACCESS_KEY")
ACCESS_KEY_SECRET = os.environ.get("ACCESS_KEY_SECRET")

def tweet(text):
    #using tweepy library to get access to account
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_KEY_SECRET)

    #tweet with the text
    api = tweepy.API(auth)
    api.update_status(text)
