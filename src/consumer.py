# consumer.py

# description
# listens to a topic

# import statements
from kafka import KafkaConsumer
import json

# Create a consumer instance, subscribing to a topic
def consumer_message(message):
    consumer = KafkaConsumer(
        'my_topic',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest', # Start from the earliest message
        enable_auto_commit=True,
        group_id='my_group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')) # Deserialize JSON data
    )

    # Read and print messages
    for message in consumer:
        print(f"Received message: {message.value}")
