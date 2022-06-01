import re
import numpy as np
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
import awswrangler as wr
import boto3

def tweet_sentiment(tweet_df):
    score,sentiment=[],[]
    for i in range(len(tweet_df['text'])):
        score = analyzer.polarity_scores(tweet_df['text'][i])
        score = score['compound']
        score.append(score)
    
    for i in score:
        if i>=0.05:
            sentiment.append('Positive')
        elif i <= (-0.05):
            sentiment.append('Negative')
        else:
            sentiment.append('Neutral')
    tweet_df['score'] = pd.Series(np.array(score))
    tweet_df['sentiment'] = pd.Series(np.array(sentiment))
    return tweet_df

def clean(tweet):
    whitespace = re.compile(r"\s+")
    alpha = re.compile(r"[^a-zA-Z0-9 \n\.]")
    web_address = re.compile(r"(?i)http(s):\/\/[a-z0-9.~_\-\/]+")
    tesla = re.compile(r"(?i)@Tesla(?=\b)")
    user = re.compile(r"(?i)@[a-z0-9_]+")
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  
        u"\U0001F300-\U0001F5FF"  
        u"\U0001F680-\U0001F6FF"  
        u"\U0001F1E0-\U0001F1FF"        
                                "]+", flags=re.UNICODE)
    my_regex = [ whitespace, alpha, web_address, tesla, user, regrex_pattern ]
    for rege in my_regex:
        tweet = rege.sub('  ', tweet)
    
    return tweet

def write_raw_tweets_to_s3(my_df,raw_tweets):
        wr.s3.to_parquet(
            df=my_df,
            path=raw_tweets,
            dataset=True,
            # partition_cols=['datetime'],
            # database='tweets_db',   #   Athena/Glue database
            # table='tweets_table1'   #   Athena/Glue table
        )
        print("DONE WRITTING RAW TWEETS")
        return True
