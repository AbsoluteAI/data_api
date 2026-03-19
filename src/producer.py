# producer.py

# description
# sends JSON data to a topic

# import statements
from kafka import KafkaProducer
import json

def producer_message(message):
    # Create a producer instance, specifying bootstrap servers and a value serializer
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    # Send a message to a topic
    producer.send('my_topic', {'key': 'value'})
    producer.flush() # Ensure all messages are sent before exiting