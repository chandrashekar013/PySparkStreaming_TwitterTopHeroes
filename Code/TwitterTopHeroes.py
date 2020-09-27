import tweepy


# Class which performs action
class TwitterTopHeroes(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)


# Enter the Twitter credentials
consumer_key = '[Enter Consumer Key]'
consumer_secret = '[Enter Consumer Secret]'
access_token = '[Enter Access Token]'
access_token_secret = '[Enter Access Token Secret]'

# Set Twitter Properties on auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Pass auth as parameter into Tweepy(Python library for Twitter)
api = tweepy.API(auth)
twitterTopHeroes = TwitterTopHeroes()

# Pass the auth to authenticate with Twitter and listener class where the action is performed to
# get back Stream from Twitter which can then be used to filter messages

topHeroes = tweepy.Stream(auth=api.auth, listener=twitterTopHeroes)
topHeroes.filter(track=['urstrulyMahesh', 'kchirutweets', 'iamnagarjuna', 'venkymama', 'RGVzoomin'])
