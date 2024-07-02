# from fastapi import FastAPI, Response, BackgroundTasks, HTTPException
# from aiokafka import AIOKafkaProducer, AIOKafkaConsumer, errors 
# import asyncio
# import logging

# # KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "default_topic")
# # KAFKA_BOOTSTRAP_SERVER = os.getenv("KAFKA_BOOTSTRAP_SERVER", "localhost:9092")

# app = FastAPI()
# logger = logging.getLogger("uvicorn.error")

# loop = asyncio.get_event_loop()
# producer = AIOKafkaProducer(loop=loop, bootstrap_servers='localhost:9092')

# consumed_messages = []
# filtered_messages = []

# @app.on_event("startup")
# async def on_startup():
#     try:
#         await producer.start()
#         logger.info("Kafka producer started")
#         asyncio.create_task(consume())
#         logger.info("Kafka consumer task created")
#     except errors.KafkaConnectionError as e:
#         logger.error(f"Kafka connection error: {e}")


# @app.on_event("shutdown")
# async def on_shutdown():
#     await producer.stop()
#     logger.info("Kafka producer stopped")

# @app.post("/send/{topic}")
# async def produce(topic: str, message: str):
#     try:
#         await producer.send_and_wait(topic, message.encode('utf-8'))
#         logger.info(f"Produced message: {message} to topic: {topic}")
#         return {"message": "Message sent successfully"}
#     except errors.KafkaConnectionError as e:
#         logger.error(f"Kafka connection error: {e}")
#         return {"message": "Failed to send message"}

# async def consume():
#     consumer = AIOKafkaConsumer(
#         'my_topic',
#         loop=loop,
#         bootstrap_servers='localhost:9092',
#         group_id="my-group")
#     await consumer.start()
#     try:
#         async for msg in consumer:
#             message = msg.value.decode('utf-8')
#             topic = msg.topic
#             consumed_messages.append({"topic": topic, "message": message})
#             logger.info(f"Consumed message: {message} from topic: {topic}")
#             # Filtering
#             if "important" in message.lower():
#                 filtered_messages.append({"topic": topic, "message": message})
#                 logger.info(f"Filtered message: {message} from topic: {topic}")
#     except Exception as e:
#         logger.error(f"Error occurred: {e}")
#     finally:
#         await consumer.stop()


# @app.get("/messages")
# def get_messages():
#     logger.info(f"Returning consumed messages: {consumed_messages}")
#     return {"messages": consumed_messages}

# @app.get("/filtered_messages")
# def get_filtered_messages():
#     logger.info(f"Returning filtered messages: {filtered_messages}")
#     return {"messages": filtered_messages}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)










import time
from fastapi import FastAPI, Response, BackgroundTasks, HTTPException
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer, errors, AIOKafkaClient
import asyncio
import logging
import os


# KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "default_topic")
KAFKA_BOOTSTRAP_SERVER = os.getenv("KAFKA_BOOTSTRAP_SERVER", "localhost:9092")

app = FastAPI()
logger = logging.getLogger("uvicorn.error")

# All the data topics
topics = ["PersonFell", "BrokenGlass", "DirtyTable", "Brawl", "MissingRings", "MissingBride", "MissingGroom", "FeelingIll", "InjuredKid", "NotOnTheList", "BadFood", "MusicTooLoud", "MusicTooLow"]

loop = asyncio.get_event_loop()
producer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVER)

consumed_messages = []
catering_messages = []
waiters_messages = []

@app.on_event("startup")
async def on_startup():
    try:
        await producer.start()
        logger.info("Kafka producer started")
        asyncio.create_task(consume_all())
        asyncio.create_task(consume_catering())
        asyncio.create_task(consume_waiters())
        logger.info("Kafka consumer tasks catering and waiters created")
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

async def consume_all():
    consumer = AIOKafkaConsumer(
        *topics, # Unpack all topic names
        loop=loop,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        group_id= "AllConsumers")
    await consumer.start()
    try:
        async for msg in consumer:
            message = msg.value.decode('utf-8')
            topic = msg.topic
            consumed_messages.append({"topic": topic, "message": message})
            logger.info(f"Consumed_all message: {message} from topic: {topic}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await consumer.stop()

async def consume_catering():
    consumer = AIOKafkaConsumer(
        'FeelingIll', #Sub in KAFA_TOPIC later
        #Add other topics here
        loop=loop,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        group_id="Catering")
    await consumer.start()
    try:
        async for msg in consumer:
            message = msg.value.decode('utf-8')
            topic = msg.topic
            catering_messages.append({"topic": topic, "message": message})
            logger.info(f"Catering message: {message} from topic: {topic}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await consumer.stop()

async def consume_waiters():
    consumer = AIOKafkaConsumer(
        'FeelingIll',#Sub in KAFA_TOPIC later
        #Add other topics here
        loop=loop,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        group_id="Waiters")
    await consumer.start()
    try:
        async for msg in consumer:
            message = msg.value.decode('utf-8')
            topic = msg.topic
            waiters_messages.append({"topic": topic, "message": message})
            logger.info(f"Waiting message: {message} from topic: {topic}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await consumer.stop()


@app.get("/messages")
def get_messages():
    logger.info(f"Returning consumed messages: {consumed_messages}")
    return {"All messages": consumed_messages}

@app.get("/waiters_messages")
def get_waiters_messages():
    logger.info(f"Returning consumed messages: {consumed_messages}")
    return {"waiters messages": waiters_messages}

@app.get("/catering_messages")
def get_catering_messages():
    logger.info(f"Returning consumed messages: {consumed_messages}")
    return {"catering messages": catering_messages}

