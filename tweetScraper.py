"""
Name: Kevin G. Fuentes
Date-Started: November 2, 2018, 1:20pm
Date-Finished: November 2, 2018, 6:23pm
Partner: Jeff Zeejay Belamide

Feature(s):
    (i) Can scrape tweets from any user specified,
    (ii) Can scrape number of tweets specified,
    (iii) Prints the full content of tweets and retweets.

API used: Tweepy
"""
import tweepy

#My Account credentials
consumer_key = 'Avjn39ijpgwvbPjGk1mgOcacP'
consumer_secret = 'YHkIWlTA3rQIaK66RNRr7vj8YO6rzGYfJTItLZeJU6gKAhVHDo'
access_token = '1056776408452616193-NgVyflfUxLP3YRnSxKs7F9hBts69U9'
access_token_secret = 'cVCfipIqrGXCBEmpXOKnt1AIlWheGWE3EZhmUidYiE061'

# Authorization to consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)
#Calling API
api = tweepy.API(auth)
#Asking for the screen name
screenName = input("Please Enter Screen Name (Example: @jeexpoy): @")
#Asking the number of tweets the user want to print
number_of_tweets= int(input("Please Enter the No. of Tweets to be Printed: "))

print('\nNow printing', number_of_tweets, 'Tweets from @', screenName, ':\n')
"""
Make initial request for tweets indicated by screenName(User-Indicator),
number_of_tweets(the maximum allowed count), include_rts set to true(Includes retweets),
and tweet_mode set to extended(Allow to get the full text of Tweets)
"""
if number_of_tweets <= 200:
    tweets = api.user_timeline(screen_name = screenName, count = number_of_tweets, include_rts = True, tweet_mode = 'extended') # 200 limit of tweets
elif number_of_tweets <= 3200:
    tweets = tweepy.Cursor(api.user_timeline, screen_name = screenName, include_rts = True, tweet_mode = 'extended').items(number_of_tweets) # 3200 limit of tweets
else:
    pass

all_tweets = []
[all_tweets.append(tweet) for tweet in tweets] #add every tweet to the all_tweet list
#printing the tweets
counter = 1
for tweet in all_tweets:
    try:
        if tweet.retweeted_status: #Condition to check if there are any retweet status.
            print('Tweet No.',counter, '\n', tweet.retweeted_status.full_text, '\n') #tweets.retweeted_status.full_text prints the full text of the retweet.
            counter+=1
    except:
        print('Tweet No.',counter, '\n', tweet.full_text, '\n') #tweets.full_text prints the full text of the tweet.
        counter+=1
