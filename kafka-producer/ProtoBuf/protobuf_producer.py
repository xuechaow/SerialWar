#! /usr/bin/python
## pip install kafka-python
# make sure kakfa and avro modules are properly installed
from kafka.producer import KafkaProducer
import person_pb2
import io, random
import json
import time
import sys

# Send all data to the 3 partitions of Kafka 
class Producer():
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=["52.41.44.90:9092","52.36.206.57:9092","52.40.205.225:9092"],acks=0,linger_ms=500)
    def produce_msgs(self,msg_list):
    while True:
        index = random.randrange(0,999)
            info = person_pb2.PersonInfo()
            serialize_protobuf (info.user.add(), msg_list[index])
            _msg = user.SerializeToString()
            self.producer.send(topic, _msg)


# This function fills in a Person message with a slice of JSON.
def serialize_protobuf(user, json_msg:
    user.id = json_msg.id
    user.first_name = json_msg.first_name
    user.last_name = json_msg.last_name
    user.email = json_msg.email
    user.gender = json_msg.gender
    user.City = json_msg.City
    user.Company = json_msg.Company
    user.Country = json_msg.Country
    user.SSN = json_msg.SSN

# main procedure: randomly select a piece of info, serialize it with
# protobuf, then send it to kafka
if __name__ == "__main__":

    #Synthesized JSON data
    file = open("MOCK_DATA.json")
    str = file.read()
    message_list = json.loads(str)
 
    # Kafka topic
    topic = "protobuf"

    args = sys.argv
    prod = Producer()
    prod.produce_msgs(message_list)

 





