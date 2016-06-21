import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sc = SparkContext(appName="PythonStreamingKafkaPrintTwitter")
ssc = StreamingContext(sc, 1)
zkQuorum = 'ec2-52-40-205-225.us-west-2.compute.amazonaws.com:2181'
topic = 'my-topic'
kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1})
lines = kvs.map(lambda x: x[1])
content = lines.collect()
print (content)

ssc.start()
ssc.awaitTermination()
