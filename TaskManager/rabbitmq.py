import os
import pika

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost/")

params = pika.URLParameters(RABBITMQ_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='task_notifications')

def send_notification(message: str):
    channel.basic_publish(exchange='', routing_key='task_notifications', body=message)

def close_connection():
    connection.close()

    