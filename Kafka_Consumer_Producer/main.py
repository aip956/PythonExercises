from fastapi import FastAPI, Response, BackgroundTasks
# Removing next line to enable streaming; importing confluent_kafka instead
# from aiokafka import AIOKafkaProducer, AIOKafkaConsumer, errors 
from confluent_kafka import Consumer, Producer, KafkaError
# import asyncio
import logging
import json

app = FastAPI()
logger = logging.getLogger("uvicorn.error")
logging.basicConfig(level=logging.INFO)

# producer_conf = {
#     'bootstrap.servers': 'localhost:9092'
# }
# producer = Producer(**producer_conf)

consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(**consumer_conf)
consumer.subscribe(['my_topic'])

@app.get("/stream/{keyword}")
async def stream_messages(keyword: str):
    def event_generator():
        while True:
            msg = consumer.poll(1.0) # Poll for a message (timeout after 1 second)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    logger.info('%% %s [%d] reached end at offset %d\n' %
                        (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                # Message is a normal message
                message = json.loads(msg.value().decode('utf-8'))
                if keyword.lower() in message.get("comment", "").lower():
                    yield f"data: {json.dumps(message)}\n\n"
    return Response(content=event_generator(), media_type="text/event-stream")

                    # logger.error(f"Error occurred: {msg.error()}")
                    # break

def filter_message(message):
    """filter function to check temperature."""
    try:
        data = json.loads(message)
        # Filter condition: temperature > 30
        if data.get('temperature', 0) > 30.0:
            return high_temp_topic
        else:
            return normal_temp_topic
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
        return None
    
def delivery_report(err, msg):
    """Delivery report for Kafka producer."""
    if err is not None:
        logger.error(f'Message delivery failed: {err}')
    else:
        logger.info(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# loop = asyncio.get_event_loop()
# producer = AIOKafkaProducer(loop=loop, bootstrap_servers='localhost:9092')

# consumed_messages = []

@app.on_event("startup")
async def on_startup():
    try:
        await producer.start()
        logger.info("Kafka producer started")
        asyncio.create_task(consume())
        logger.info("Kafka consumer task created")
    except errors.KafkaConnectionError as e:
        logger.error(f"Kafka connection error: {e}")


@app.on_event("shutdown")
async def on_shutdown():
    await producer.stop()
    logger.info("Kafka producer stopped")

@app.post("/send/{topic}")
async def produce(topic: str, message: str):
    try:
        await producer.send_and_wait(topic, message.encode('utf-8'))
        logger.info(f"Produced message: {message} to topic: {topic}")
        return {"message": "Message sent successfully"}
    except errors.KafkaConnectionError as e:
        logger.error(f"Kafka connection error: {e}")
        return {"message": "Failed to send message"}

async def consume():
    consumer = AIOKafkaConsumer(
        'my_topic',
        loop=loop, 
        bootstrap_servers='localhost:9092',
        group_id="my-group")
    await consumer.start()
    try:
        async for msg in consumer:
            message = msg.value.decode('utf-8')
            topic = msg.topic
            consumed_messages.append({"topic": topic, "message": message})
            logger.info(f"Consumed message: {message} from topic: {topic}")
    finally:
        await consumer.stop()


@app.get("/messages")
def get_messages():
    logger.info(f"Returning consumed messages: {consumed_messages}")
    return {"messages": consumed_messages}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

#  Adding a change
# Another change