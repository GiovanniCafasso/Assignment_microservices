from kafka import KafkaConsumer
consumer = KafkaConsumer('notification_borrowing', bootstrap_servers=['kafka:9092'])
for msg in consumer:
    print (msg)