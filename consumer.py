from kafka import KafkaConsumer
import json

if __name__=="__main__":
    consumer = KafkaConsumer(
        "registered_user",
        bootstrap_servers='10.0.2.15:9092',
        auto_offset_reset = 'earliest',
        group_id = "condumer-group-a"
    )
    print("Starting the consumer")
    for msg in consumer:
        print("Registered user:{}".format(json.loads(msg.value)))