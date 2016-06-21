from kafka.producer import KafkaProducer
import avro.schema
import io, random
from avro.io import DatumWriter
import json
import time
import sys

file = open("MOCK_DATA.json")
str = file.read()
message_list = json.loads(str)
 
# Kafka topic
topic = "Raw-JSON"
 
class Producer():
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=["52.41.44.90:9092","52.36.206.57:9092","52.40.205.225:9092"],acks=0,linger_ms=500)
    def produce_msgs(self,msg_list):
	while True:
		index = random.randrange(0,999)
    		json_msg =json.dumps(msg_list[index]).encode('utf-8')
    		self.producer.send(topic, json_msg)

if __name__ == "__main__":
    args = sys.argv
    prod = Producer()
    prod.produce_msgs(message_list)

 
