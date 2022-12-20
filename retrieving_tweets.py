import tweepy

# Have to replace these with API keys and secrets
consumer_key = "MY_CONSUMER_KEY"
consumer_secret = "MY_CONSUMER_SECRET"
access_key = "MY_ACCESS_KEY"
access_secret = "MY_ACCESS_SECRET"

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_key, access_secret)
api = tweepy.API(auth)

# Retrieve tweets from user's home timeline
tweets = api.home_timeline()

for tweet in tweets:
  print(tweet.text)
