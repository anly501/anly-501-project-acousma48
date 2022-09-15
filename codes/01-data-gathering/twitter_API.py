#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install tweepy')


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import os
import time
import requests
import json
import csv
from tqdm import tqdm
import tweepy


# In[3]:


consumer_key = 'OA4CTZkyLwMOg08PlFt0goCNC'
consumer_secret = '8k59TeAGeqlHXjf4wjOjrKLYXpEvutuRgDjLxVxm5R7uC5wB0q'
access_token = '1177285260242874368-QoMZGUj2TsbkXyPQ5o0pu5iFrFT72q'
access_token_secret = '6JWjo6Ro4RmqIBFLjOop9QW1FCgHZltRTz8EIsj9UiMOE'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAISeXgEAAAAANwEgP0gtkLS%2Bjv9qCa3pIB3o1xs%3D98KYFXJI2DYHslg3StyrI2h9aB0w8PYq8iJyGS6Vdwsrhgkt7r'


# In[4]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# In[ ]:


save_file = open('example_tweets.txt', 'w',encoding="utf-8")
client = tweepy.Client(bearer_token=bearer_token)

query = "new energy"
response = client.search_recent_tweets(query)
tf_list = 'text'
tweets_responses =  tweepy.Paginator(client.search_all_tweets, query=query, tweet_fields =tf_list ,max_results=100).flatten(limit=250)

for tweet in tweepy.Paginator(client.search_all_tweets, query=query,max_results=100).flatten(limit=250):
    # print(tweet.keys)
    print(tweet.public_metrics)
    item = tweet.text.strip().replace('\n', ' ')
    save_file.write(item + '\n')
    print(item)

save_file.close()

