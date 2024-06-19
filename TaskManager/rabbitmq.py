import os
import pika
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost/")
RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://rabbitmq:local@rabbitmq:5672/")
# logger.info(f"RABBITMQ_URL: {RABBITMQ_URL}")
connected = False
attempts = 0
while not connected and attempts < 5:
    try:
        params = pika.URLParameters(RABBITMQ_URL)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.queue_declare(queue='task_notifications')
        logger.info("Connected to RabbitMQ")
        connected = True
        logger.info("Connected to RabbitMQ")
    except pika.exceptions.AMQPConnectionError as e:
        attempts += 1
        logger.error(f"Error connecting to RabbitMQ: {e}")
        time.sleep(3)


def send_notification(message: str):
    channel.basic_publish(exchange='', routing_key='task_notifications', body=message)

def close_connection():
    connection.close()

    