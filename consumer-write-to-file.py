from kafka.consumer import KafkaConsumer

# Kafka consumer configuration
topic = "my-news"
brokers = "localhost:9092"

# Create the Kafka consumer
consumer = KafkaConsumer(topic, bootstrap_servers=brokers, auto_offset_reset = 'earliest')

# save messages to file
for message in consumer:
    with open("data/data.json", "a") as f:
        f.write("{0}\n".format(message.value.decode()))
#for message in consumer:
#    print(message.value.decode())