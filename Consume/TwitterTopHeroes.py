import tweepy

consumer_key = "[insert your key here]"
consumer_secret = "[insert your secret here]"
access_key = "[insert your key here]"
access_secret = "[insert your secret here]"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=['urstrulyMahesh', 'kchirutweets', 'iamnagarjuna', 'venkymama', 'RGVzoomin'])

rdd = myStream

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#    print(tweet.text)

# user = api.get_user('twitter')
# print('screen name', user.screen_name)
# print('followers count:', user.followers_count)
