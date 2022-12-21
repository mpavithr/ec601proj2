# ec601proj2
This repository contains work for EC601 Project 2

## Phase 1 a: Twitter APIs

### Authentication and keys

Firstly, have to create a twitter developer account to get authenticated.
https://user-images.githubusercontent.com/42751267/208864517-6d7f02f6-65e5-4b03-87cf-750e5f6b3a42.PNG

Then, can get the API keys for the tests to test the API, (cutting out the keys and secret values, to keep it private)
https://user-images.githubusercontent.com/42751267/208864469-dbd61dc8-f8db-4681-80f3-6821d9170825.PNG

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

#### Results: The program successfully searches for tweets that contain the specified hashtag and prints the text of each tweet to the console.

## Phase 1 a: Google NLP APIs

### Test Program 1: Analyzing the sentiment of text strings

The objective is to analyze the sentiment of text strings. After authentication and initializng Google NLP Client, I used a text to analyze the sentiment.

#### Results: The program sucessfully prints out scores for sentiments.

### Test Program 2: Analyzing the sentiment of text on page

The objective is to analyze the sentiment of text on pages. After authentication and initializng Google NLP Client, I used a text to analyze the sentiment of a random news page.

#### Results: The program sucessfully prints out scores for sentiments.

## Phase 2: 

Social Media Analyzer: 

*Minimum Viable Product*: A social media analyzer that can analyze the sentiment of tweets and Facebook posts for a given user or topic.

*User*: A business owner or celebrity or someone who is interested in understanding the sentiment of their social media presence.

*User Stories*:

As a user, I want to be able to input a Twitter handle or hashtag to analyze the sentiment of the tweets associated with it.

As a user, I want to be able to input a Facebook page or topic to analyze the sentiment of the posts associated with it.

As a user, I want to see a visual representation of the overall sentiment analysis (e.g. a bar chart).

As a user, I want to be able to view the individual tweets or posts that were analyzed and their associated sentiment scores.

*Modular Design*:

Module 1: Twitter sentiment analysis

Module 2: Facebook/Instagram sentiment analysis

Module 3: Visual representation of sentiment analysis

Module 4: Individual tweet/post view with sentiment scores
