#
#
### pip install both dependencies
#
#
import tweepy
from textblob import TextBlob


consumer_key = 'SECRET WORD YOU WILL NEVER KNOW'
consumer_secret = 'SECRET WORD YOU WILL NEVER KNOW'

access_token = 'SECRET WORD YOU WILL NEVER KNOW'
access_token_secret = 'SECRET WORD YOU WILL NEVER KNOW'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('python')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
