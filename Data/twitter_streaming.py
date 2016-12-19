import json
import sys
import time
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from kafka.producer import KafkaProducer


ACCESS_TOKEN = '2905352843-Sm2UEyP0MmNkAU6ZMkhHcJDRrtxLN37lo6hERRB'
ACCESS_SECRET = 'zLgNeRIMHJu5y013D4DyPgAkQXq3urhfC64OznWBgGlZx'
CONSUMER_KEY = 'hBb9XKsTPAUV7QNx8b7h1E71M'
CONSUMER_SECRET = '0mqPbVbEmRIVZMqJGzaJZlejnAffcVZa3paC66qBvdaJKMkezt'

# Connect with oauth and start the streaming (array of strings)
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_stream = TwitterStream(auth=oauth)
tweet_stream_source = twitter_stream.statuses.sample()

# Import from Kafka.producer
class Producer():

    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers = 'localhost:9092')
    def produce_msgs(self,source):
	for drop in source:
        	if 'text' in drop:
			message = json.dumps(drop)
			self.producer.send('Twitter-Stream',message)
			print(message)
			self.producer.send('message-size',len(message))
	#	time.sleep(1)

if __name__ == "__main__":
    args = sys.argv
    #dns = str(args[1])
    prod = Producer()
    prod.produce_msgs(tweet_stream_source)
