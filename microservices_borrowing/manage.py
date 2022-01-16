#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import dotenv
import kafka
from kafka.admin import KafkaAdminClient, NewTopic

def main():

    # read env
    dotenv.read_dotenv()    

    #Creating topic 'notification_borrowing' if not exist
    bool = False
    host=os.getenv("HOST_KAFKA")
    port=os.getenv("PORT_KAFKA")
    address = host + ':' + port
    consumer = kafka.KafkaConsumer(group_id='borrowing-notification', bootstrap_servers=[address])
    for topic in consumer.topics():
        if topic == 'borrowing-notification':
            bool = True
    if bool == False:
        admin_client = KafkaAdminClient(
            bootstrap_servers="kafka:9092", 
            client_id=0
        )
        topic_list = []
        topic_list.append(NewTopic(name="borrowing-notification", num_partitions=1, replication_factor=1))
        admin_client.create_topics(new_topics=topic_list, validate_only=False)   

    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'microservices_borrowing.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
