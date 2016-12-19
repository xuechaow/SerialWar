import sys
import redis
from time import gmtime, strftime
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sc = SparkContext(appName="PythonStreamingKafkaPrintTwitter")
ssc = StreamingContext(sc, 1)
zkQuorum = 'ec2-52-40-205-225.us-west-2.compute.amazonaws.com:2181'
topic = 'my-topic'
kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1})
lines = kvs.map(lambda x:x[1])
#lines.pprint()

redis_entry = redis.Redis(host = 'ec2-52-39-137-189.us-west-2.compute.amazonaws.com', port = 6379,db = 0)

def echo(rdd):
	rddstr = rdd.take(1)
	time = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
	if(len(rddstr)>0):
		d_str = ''.join(rddstr[0])
		print('||||||||||'+str(hash(time)%1000)+'|||||||||||||||||||')
		print('--------\n'+d_str+'\n-----------------')
		redis_entry.set(hash(time)%1000, d_str)
   	
lines.foreachRDD(echo)

ssc.start()
ssc.awaitTermination()
