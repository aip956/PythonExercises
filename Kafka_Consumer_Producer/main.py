from fastapi import FastAPI, Response, BackgroundTasks, HTTPException
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer, errors, AIOKafkaClient
import asyncio
import logging
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

KAFKA_BOOTSTRAP_SERVER = os.getenv("KAFKA_BOOTSTRAP_SERVER", "localhost:9092")

app = FastAPI()
logger = logging.getLogger("uvicorn.error")

# Database setup
DATABASE_URL = "postgresql://user:password@postgresserver/db"
# Database instance
database = Database(DATABASE_URL)
# Engine and session factory
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
# Create a base class for declarative models
Base = declarative_base()

# Define the models for each topic table in db

class ConsumedMessage(Base):
    __tablename__ = 'consumed_messages'
    id = Column(Integer, primary_key=True)
    topic = Column(String)
    message = Column(String)

class PersonFell(Base):
    __tablename__ = "person_fell"
    id = Column(Integer, primary_key=True)
    message = Column(String)

class BrokenGlass(Base):
    __tablename__ = "broken_glass"
    id = Column(Integer, primary_key=True)
    message = Column(String)

class DirtyTable(Base):
    __tablename__ = "dirty_table"
    id = Column(Integer, primary_key=True)
    message = Column(String)

class Brawl(Base):
    __tablename__ = "brawl"
    id = Column(Integer, primary_key=True)
    message = Column(String)

class MissingRings(Base):
    __tablename__ = "missing_rings"
    id = Column(Integer, primary_key=True)
    message = Column(String)

class MissingBride(Base):
    __tablename__ = "missing_bride"
    id = Column(Integer, primary_key=True)
    message = Column(String)

class MissingGroom(Base):
    __tablename__ = "missing_groom"
    id = Column(Integer, primary_key=True)
    message = Column(String)

class FeelingIll(Base):
    __tablename__ = "feeling_ill"
    id = Column(Integer, primary_key=True)
    message = Column(String)    

class InjuredKid(Base):
    __tablename__ = "injured_kid"
    id = Column(Integer, primary_key=True)
    message = Column(String)

class NotOnList(Base):
    __tablename__ = "not_on_list"
    id = Column(Integer, primary_key=True)
    message = Column(String)

class BadFood(Base):
    __tablename__ = "bad_food"
    id = Column(Integer, primary_key=True)
    message = Column(String)

class MusicTooLoud(Base):
    __tablename__ = "music_too_loud"
    id = Column(Integer, primary_key=True)
    message = Column(String)

class MusicTooLow(Base):
    __tablename__ = "music_too_low"
    id = Column(Integer, primary_key=True)
    message = Column(String)


# Create the tables in the database
Base.metadata.create_all(engine)








# Function to save a consumed message to the database
def save_consumed_message(topic, message):
    session = Session()
    if topic == "person_fell":
        consumed_message = PersonFell(message=message)
    elif topic == "broken_glass":
        consumed_message = BrokenGlass(message=message)
    elif topic == "dirty_table":
        consumed_message = DirtyTable(message=message)  
    elif topic == "brawl":
        consumed_message = Brawl(message=message)
    elif topic == "missing_rings":
        consumed_message = MissingRings(message=message)
    elif topic == "missing_bride":
        consumed_message = MissingBride(message=message)
    elif topic == "missing_groom":
        consumed_message = MissingGroom(message=message)
    elif topic == "feeling_ill":
        consumed_message = FeelingIll(message=message)
    elif topic == "injured_kid":
        consumed_message = InjuredKid(message=message)
    elif topic == "not_on_list":
        consumed_message = NotOnList(message=message)
    elif topic == "bad_food":
        consumed_message = BadFood(message=message)
    elif topic == "music_too_loud":
        consumed_message = MusicTooLoud(message=message)
    elif topic == "music_too_low":
        consumed_message = MusicTooLow(message=message)
    else:
        # Handle unknown topic
        session.close()
        return
    # consumed_message = ConsumedMessage(topic=topic, message=message)
    session.add(consumed_message)
    session.commit()
    session.close()




# All the data topics
topics = ["person_fell", "broken_glass", "dirty_table", "brawl", "missing_rings", "missing_bride", "missing_groom", "feeling_ill", "injured_kid", "not_on_list", "bad_food", "music_too_loud", "music_too_low"]
SECURITY_TOPICS = ["brawl", "not_on_list", "person_fell", "injured_kid"]
CLEAN_UP_TOPICS = ["dirty_table", "broken_glass"]
CATERING_TOPICS = ["bad_food", "music_too_loud", "music_too_low", "feeling_ill"]
OFFICIANT_TOPICS = ["missing_rings", "missing_bride", "missing_groom"]
WAITERS_TOPICS = [ "broken_glass", "person_fell", "injured_kid", "feeling_ill"]


loop = asyncio.get_event_loop()
producer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVER)

consumed_messages = []
security_messages = []
clean_up_messages = []
catering_messages = []
officiant_messages = []
waiters_messages = []

@app.on_event("startup")
async def on_startup():
    try:
        await producer.start()
        logger.info("Kafka producer started")
        asyncio.create_task(consume_all())
        asyncio.create_task(consume_security())
        asyncio.create_task(consume_clean_up())
        asyncio.create_task(consume_catering())
        asyncio.create_task(consume_officiant())
        asyncio.create_task(consume_waiters())
        logger.info("Kafka consumer tasks created")
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
        group_id= "AllConsumers",
        session_timeout_ms = 10000, # 6 seconds
        heartbeat_interval_ms = 3000, # 2 seconds
    )
    await consumer.start()
    try:
        async for msg in consumer:
            message = msg.value.decode('utf-8')
            topic = msg.topic
            consumed_messages.append({"topic": topic, "message": message})
            save_consumed_message(topic, message)   #Save message to the right table
            logger.info(f"Consumed_all message: {message} from topic: {topic}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await consumer.stop()

async def consume_security():
    consumer = AIOKafkaConsumer(
        *SECURITY_TOPICS,
        loop=loop,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        groups_id="Security",
        session_timeout_ms=10000,
        heartbeat_interval_ms=3000,
    )
    await consumer.start()
    try:
        async for msg in consumer:
            message = msg.value.decode('utf-8')
            topic = msg.topic
            security_messages.append({"topic": topic, "message": message})
            save_consumed_message(topic, message)  # Save message to the appropriate table
            logger.info(f"Security message: {message} from topic: {topic}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await consumer.stop()

async def consume_clean_up():
    consumer = AIOKafkaConsumer(
        *CLEAN_UP_TOPICS,
        loop=loop,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        group_id="Clean_Up",
        session_timeout_ms=10000,
        heartbeat_interval_ms=3000,
    )
    await consumer.start()
    try:
        async for msg in consumer:
            message = msg.value.decode('utf-8')
            topic = msg.topic
            clean_up_messages.append({"topic": topic, "message": message})
            save_consumed_message(topic, message)  # Save message to the appropriate table
            logger.info(f"Clean_Up message: {message} from topic: {topic}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await consumer.stop()


async def consume_catering():
    consumer = AIOKafkaConsumer(
        *CATERING_TOPICS, #Sub in KAFA_TOPIC later
        loop=loop,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        group_id="Catering",
        session_timeout_ms=10000,
        heartbeat_interval_ms=3000,
    )
    await consumer.start()
    try:
        async for msg in consumer:
            message = msg.value.decode('utf-8')
            topic = msg.topic
            catering_messages.append({"topic": topic, "message": message})
            save_consumed_message(topic, message)  # Save message to the appropriate table
            logger.info(f"Catering message: {message} from topic: {topic}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await consumer.stop()

async def consume_officiant():
    consumer = AIOKafkaConsumer(
        *OFFICIANT_TOPICS,
        loop=loop,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        group_id="Officiant",
        session_timeout_ms=10000,
        heartbeat_interval_ms=3000,
    )
    await consumer.start()
    try:
        async for msg in consumer:
            message = msg.value.decode('utf-8')
            topic = msg.topic
            officiant_messages.append({"topic": topic, "message": message})
            save_consumed_message(topic, message)  # Save message to the appropriate table
            logger.info(f"Officiant message: {message} from topic: {topic}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await consumer.stop()

async def consume_waiters():
    consumer = AIOKafkaConsumer(
        *WAITERS_TOPICS,
        loop=loop,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        group_id="Waiters",
        session_timeout_ms=10000,
        heartbeat_interval_ms=3000,
    )
    await consumer.start()
    try:
        async for msg in consumer:
            message = msg.value.decode('utf-8')
            topic = msg.topic
            waiters_messages.append({"topic": topic, "message": message})
            save_consumed_message(topic, message)  # Save message to the appropriate table
            logger.info(f"Waiting message: {message} from topic: {topic}")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await consumer.stop()


@app.get("/messages")
def get_messages():
    logger.info(f"Returning consumed messages: {consumed_messages}")
    return {"All messages": consumed_messages}

@app.get("/security_messages")
def get_security_messages():
    logger.info(f"Returning security messages: {security_messages}")
    return {"security messages": security_messages}

@app.get("/clean_up_messages")
def get_clean_up_messages():
    logger.info(f"Returning clean_up messages: {clean_up_messages}")
    return {"clean_up messages": clean_up_messages}

@app.get("/catering_messages")
def get_catering_messages():
    logger.info(f"Returning catering messages: {catering_messages}")
    return {"catering messages": catering_messages}

@app.get("/officiant_messages")
def get_officiant_messages():
    logger.info(f"Returning officiant messages: {officiant_messages}")
    return {"officiant messages": officiant_messages}

@app.get("/waiters_messages")
def get_waiters_messages():
    logger.info(f"Returning waiter messages: {waiters_messages}")
    return {"waiters messages": waiters_messages}