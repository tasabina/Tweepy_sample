import tweepy
import io
import json

consumer_key = '***'
consumer_secret = '***'
access_token = '***'
access_token_secret = '***'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user_new = api.user_timeline(screen_name)

for itemsy in user_new:
    tweet_file = open('tweeter.txt', 'a')
    tweet_file.write(str(itemsy.text)+'\n'+'Retweet: '
                                           ''+str(itemsy.retweet_count)+';'+'Favorite: '
                                                                            ''+str(itemsy.favorite_count)+'\r\n')
    tweet_file.close()



