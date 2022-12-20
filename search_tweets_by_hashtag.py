import tweepy

# Replace with the API keys and secrets
consumer_key = "MY_CONSUMER_KEY"
consumer_secret = "MY_CONSUMER_SECRET"
access_key = "MY_ACCESS_KEY"
access_secret = "MY_ACCESS_SECRET"

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_key, access_secret)
api = tweepy.API(auth)

# Search for tweets containing the hashtag "python"
tweets = api.search(q="#python", lang="en")

for tweet in tweets:
  print(tweet.text)



