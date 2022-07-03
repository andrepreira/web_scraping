
import pandas as pd
from dotenv import load_dotenv
import tweepy as tw
import time
load_dotenv()
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

from my_functions import functions

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
acess_token = os.environ.get("acess_token")
acess_token_secret = os.environ.get("acess_token_secret")
output_file = os.environ.get("output_file")

# Tweeter API

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acess_token, acess_token_secret)
api = tw.API(auth)

# create empty df

tesla_df = pd.DataFrame(columns=['datetime', 'id', 'username', 'followers_count', 'verified_status',
                                 'text', 'retweets', 'tweet_url', 'location'])

print(tesla_df)
tweets_list = []
st = time.time()
