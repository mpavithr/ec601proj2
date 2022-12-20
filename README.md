# ec601proj2
This repository contains work for EC601 Project 2

## Phase 1 a: Twitter APIs

### Test Program 1: Retrieving Tweets

The objective is to retrieve a list of tweets from a specific user's timeline.

Firstly, I had to set up the necessary authentication and authorization to access the Twitter API.

Then I used the GET statuses/user_timeline endpoint to retrieve a list of tweets from the desired user's timeline.

Then I specified the user's screen name in the endpoint parameters and set the number of tweets to retrieve using the count parameter.

I executed the API request and stored the response in a variable and iterated through the list of tweets in the response and printed the text of each tweet to the console.

#### Results: The program successfully retrieves a list of tweets from the specified user's timeline and prints the text of each tweet to the console.

### Test Program 2: Searching by Time

The objective is to search for tweets that were created within a specific time frame.

Similar to the first test, I had set up the necessary authentication and authorization to access the Twitter API and used the GET search/tweets endpoint to search for tweets that were created within a specific time frame.

I specified the desired time frame using the since and until parameters in the endpoint.

I executed the API request and stored the response in a variable.

I iterated through the list of tweets in the response and print the text of each tweet to the console.

#### Results: The program successfully searches for tweets that were created within the specified time frame and prints the text of each tweet to the console.

### Test Program 3: Searching by Hashtag

The objective is to search for tweets that contain a specific hashtag.

After authentication and using the GET API, I specified the desired hashtag using the q parameter in the endpoint.

I executed the API request and stored the response in a variable.

I iterated through the list of tweets in the response and print the text of each tweet to the console.

####Results: The program successfully searches for tweets that contain the specified hashtag and prints the text of each tweet to the console.
