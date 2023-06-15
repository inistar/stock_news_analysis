from kafka import KafkaProducer
from cgi import log
import json


class Kafka:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            # value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("Initialized producer....")

    def on_send_success(self, record_metadata):
        print(f'Topic: {record_metadata.topic}, Partition: {record_metadata.partition}, Offset: {record_metadata.offset}')

    def on_send_error(self, excp):
        log.error('Error: ', exc_info=excp)

    def send(self, topic, key, value):
        self.producer.send(topic=topic, key=key, value=value).add_callback(self.on_send_success).add_errback(self.on_send_error)

    def flush(self):
        self.producer.flush()
