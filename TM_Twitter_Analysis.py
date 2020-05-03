# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:02:51 2020

@author: Abhinav
"""
#Import Libraries
import tweepy
from textblob import TextBlob

#Twitter Authentication
consumer_key = 'T4gcarK7j66B1RrWVBOr39rl4'
consumer_secret = 'xpBnInfYtdjqPXhQZeZMvJqCnt5S6FnY3HVYhPSBYaJ8cUAwjx'
access_token = '1212320988563558406-cevIttMGKByyeZThIq9ki7fguw7IKd'
access_token_secret = 'cpykrsZPLowsxzzrZob5zqaR7BEp4cCLgWCIsaMmmzNtL'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Reading data from twitter
api = tweepy.API(auth)
public_tweets = api.search('Donald Trump')

#Printing the data read from twitter
for tweet in public_tweets:
    print(tweet.text)
    
#Performing Sentiment Analysis
    analysis = TextBlob(tweet.text)
    type(analysis)
    print(analysis.sentiment)
