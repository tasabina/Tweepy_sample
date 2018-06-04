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

user_new = tweepy.Cursor(api.user_timeline).items()
user_tweets = api.get_user(screen_name)
status = api.get_status(user_tweets.status.id)
user_favorites = api.favorites(screen_name)
retweets_tweets = api.retweets(user_tweets.status.id)

json_data = json.dumps(user_tweets._json['id'])
parsed_json = json.loads(json_data)

for tweet in user_tweets._json:
    print(tweet)
    print(parsed_json)

for itemsy in user_new:
    tweet_file = open('tweeter.txt', 'a')
    tweet_file.write(str(itemsy.text)+'\n'+'Retweet: '
                                           ''+str(itemsy.retweet_count)+';'+'Favorite: '
                                                                            ''+str(itemsy.favorite_count)+'\r\n')
    tweet_file.close()


