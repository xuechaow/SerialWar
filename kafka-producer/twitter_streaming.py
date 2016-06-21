import json
import sys
import time
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from kafka.producer import KafkaProducer


ACCESS_TOKEN = '2905352843-Sm2UEyP0MmNkAU6ZMkhHcJDRrtxLN37lo6hERRB'
ACCESS_SECRET = 'zLgNeRIMHJu5y013D4DyPgAkQXq3urhfC64OznWBgGlZx'
CONSUMER_KEY = 'hBb9XKsTPAUV7QNx8b7h1E71M'
CONSUMER_SECRET = '0mqPbVbEmRIVZMqJGzaJZlejnAffcVZa3paC66qBvdaJKMkezt'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)
tweet_stream_source = twitter_stream.statuses.sample()

class Producer():

    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=["52.41.44.90:9092","52.36.206.57:9092","52.40.205.225:9092"],acks=0,linger_ms=500)
    def produce_msgs(self,source):
	for drop in source:
        	if 'text' in drop:
			message = json.dumps(v).encode('utf-8')
			self.producer.send('raw-json',message)
	#	time.sleep(1)

if __name__ == "__main__":
    args = sys.argv
    prod = Producer()
    prod.produce_msgs(tweet_stream_source)
