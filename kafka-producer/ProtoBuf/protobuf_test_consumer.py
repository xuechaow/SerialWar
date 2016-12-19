# Test producer
from kafka import KafkaConsumer
import person_pb2
import io
 
# To consume messages
consumer = KafkaConsumer('Topic-Narrow',
                         group_id='my_group',
                         bootstrap_servers=['localhost:9092'])
# deserialization with proto file
for msg in consumer:
    info = person_pb2.User()
    info.ParseFromString(msg)
    print info
