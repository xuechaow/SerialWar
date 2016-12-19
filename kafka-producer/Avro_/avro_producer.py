from kafka import SimpleProducer, KafkaClient
import avro.schema
import io, random
from avro.io import DatumWriter
import json

## Main procedure: read from data file, randomly pick one chunk of data
# use the avro schema to serialize it and send to kafka broker

file = open("MOCK_DATA.json")
str = file.read()
message_list = json.loads(str)

# To send messages synchronously
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)
 
# Kafka topic
topic = "avro"
 
# Path to user.avsc avro schema
schema_path="user.avsc"
schema = avro.schema.parse(open(schema_path).read())
 
 
while True:

    index = random.randrange(0,999)
    json_msg = message_list[index]
    producer.send_messages(topic, raw_bytes)
