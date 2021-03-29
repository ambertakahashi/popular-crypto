import config
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import collections

import tweepy as tw
import nltk
from nltk.corpus import stopwords
import re
import networkx

import warnings
warnings.filterwarning("ignore")

sns.set(font_scale=1.5)
sns.set_style("whitegrid")

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_term = "#dogecoin -filter:retweets"

tweets = tw.Cursor(api.search, q=search_term, lang="en", since='2020-03-21').items(1,000)

all_tweets = [tweet.text for tweet in tweets]

all_tweets[:5]

def remove_url(txt):
     """Replace URLs found in a text string with nothing 
     (i.e. it will remove the URL from the string).

     Parameters
     ----------
     txt : string
         A text string that you want to parse and remove urls.

     Returns
     -------
     The same txt string with url's removed.
     """

     return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

all_tweets_no_urls = [remove_url(tweet) for tweet in all_tweets]
all_tweets_no_urls[:5]
