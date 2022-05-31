
import pandas as pd
from dotenv import load_dotenv
import tweepy as tw
import time
load_dotenv()
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()