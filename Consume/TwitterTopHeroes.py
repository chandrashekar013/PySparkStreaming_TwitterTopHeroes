import tweepy

consumer_key = 'dOHiV1vYFQjA4Zixo4SHP4ZxU'
consumer_secret = 'nQe5eibr4JGRVYgyeguMz1ZEqX40cThW7C8UmIkG9XalvjhLOR'
access_token = '707230359-2tGBjJhM6tfJyEPmA7412ZukEXKaV7IVRD8BKyxo'
access_token_secret = 'UzgEILCXsnj1EPahuBOMwec3p9Yx9YHdoj4zKI6b6wGgN'

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