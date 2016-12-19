import sys
import redis
import json
import time
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

def get_RDD_Size(rdd):
	msg_list = rdd.collect()
	RDD_Size = 0
	for msg in msg_list:
		RDD_Size = RDD_Size + len(msg)
	return RDD_Size


if __name__ == "__main__":
	if len(sys.argv) != 3:
        	print("python json_consumer.py <topic> <stream window in seconds>")
        	exit(-1)
	topic,window_size = sys.argv[1:]
    	stream_rate = int(window_size)
	
	redis_entry = redis.Redis(host = 'ec2-52-39-137-189.us-west-2.compute.amazonaws.com', port = 6379,db = topic)

	sc = SparkContext(appName="JSON_Consumer")
	ssc = StreamingContext(sc, stream_rate)

	zkQuorum = 'ec2-52-40-205-225.us-west-2.compute.amazonaws.com:2181'
	kvs = KafkaUtils.createStream(ssc, zkQuorum, "json", {topic: 1})
	message_DStream = kvs.map(lambda x:x[1])
	#message_DStream.pprint()
	
   	
	#length_Stream = message_DStream.map(lambda x:{"length":get_RDD_Size(x),"time":time.time()})
	length_Stream = message_DStream.map(lambda x:{"bytes":len(x),"time":time.time()})
	length_Stream.pprint()	

	ssc.start()
	ssc.awaitTermination()
