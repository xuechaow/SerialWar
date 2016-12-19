import sys
import redis
import json
from time import gmtime, strftime
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sc = SparkContext(appName="PythonStreamingKafkaPrintTwitter")
ssc = StreamingContext(sc, 1)
zkQuorum = 'ec2-52-40-205-225.us-west-2.compute.amazonaws.com:2181'
topic = 'protobuf'
kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1})
lines = kvs.map(lambda x:x[1])
#lines.pprint()

redis_entry = redis.Redis(host = 'ec2-52-39-137-189.us-west-2.compute.amazonaws.com', port = 6379,db = 0)

def echo(rdd):
	rddstr = rdd.collect()
	time = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
	if(len(rddstr)>0):
		#print(rddstr)
		d_str = ''.join(rddstr[0])
		#print('|||||||||||')
		#print(d_str)
		#		#print(type(j_dict))
		#print j_dict['created_at'] # when the tweet posted
                #print j_dict['text'] # content of the tweet
		print('||||||||||'+str(hash(time)%1000)+'|||||||||||||||||||')
		print('--------\n'+d_str+'\n-----------------')
		j_dict = json.loads(d_str)
		print j_dict['created_at']
			
	        redis_entry.set(hash(time)%1000, j_dict)
   	
lines.foreachRDD(echo)

ssc.start()
ssc.awaitTermination()
