from fastapi import FastAPI, Response, BackgroundTasks, HTTPException
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer, errors 
import asyncio
import logging


app = FastAPI()
logger = logging.getLogger("uvicorn.error")

loop = asyncio.get_event_loop()
producer = AIOKafkaProducer(loop=loop, bootstrap_servers='localhost:9092')

consumed_messages = []
filtered_messages = []

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
            # Filtering
            if "important" in message.lower():
                filtered_messages.append({"topic": topic, "message": message})
                logger.info(f"Filtered message: {message} from topic: {topic}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await consumer.stop()


@app.get("/messages")
def get_messages():
    logger.info(f"Returning consumed messages: {consumed_messages}")
    return {"messages": consumed_messages}

@app.get("/filtered_messages")
def get_filtered_messages():
    logger.info(f"Returning filtered messages: {filtered_messages}")
    return {"messages": filtered_messages}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

