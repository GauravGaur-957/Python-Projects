import tweepy
import time

auth = tweepy.OAuthHandler(#enter your credentials here)
auth.set_access_token(#enter your access token here)

api = tweepy.API(auth)
user=api.me()

def limit(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(1000)
 

search_string= "Gaurav Gaur"
numberOfTweets=2

for tweet in tweepy.Cursor(api.search,search_string).items(numberOfTweets):
	try:
		tweet.favorite()
		print('I liked it')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
	    break	


