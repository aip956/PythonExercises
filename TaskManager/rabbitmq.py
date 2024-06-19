import pika

RABBITMQ_URL = 'amqp://guest:guest@localhost/'

connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
channel = connection.channel()

channel.queue_declare(queue='task_notifications')

def send_notification(message: str):
    channel.basic_publish(exchange='', routing_key='task_notofications', body=message)

def close_connection():
    connection.close()

    