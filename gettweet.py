import tweepy

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = "gC9UcCOayqt6DX8tSL6xkpxlX"
consumer_secret = "1x7QZ4NWeMomiGgI49xU32lwyU6WY7Lmjmr53lMpW8NCwqgCGo"
access_key = "4879261815-5aOL4yjPDq4xSTcvfpO5eRD0HhT0DPX5BFjJjzc"
access_secret = "3tAgg1sWtGSK8LtJNwzLM1KhJ6LRuLbCLBtXI4M88dmlv"

# Function to extract tweets
def get_tweets(username, number_of_tweets):

    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Access to user's access key and access secret
    auth.set_access_token(access_key, access_secret)

    # Calling api
    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name=username, count=number_of_tweets)

    # Empty Array
    tmp=[]

    # create array of tweet information: username,
    # tweet id, date/time, text
    tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
    for j in tweets_for_csv:

        # Appending tweets to the empty array tmp
        tmp.append(j)

    # Printing the tweets
    counter = 1
    for line in tmp:
        print("/*", counter ,"*/", line)
        counter += 1

# Driver code
if __name__ == '__main__':

	# Here goes the twitter handle for the user
	# whose tweets are to be extracted.
    twitter_handle = input("Enter twitter handle: ")
    number_of_tweets = int(input("Specify number of tweets: "))
    get_tweets(twitter_handle, number_of_tweets)
