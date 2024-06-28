from fastapi import FastAPI, BackgroundTasks
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import asyncio
import json

app = FastAPI()

loop = asyncio.get_event_loop()
producer = AIOKafkaProducer(loop=loop, bootstrap_servers='localhost:9092')

consumed_messages = []

@app.on_event("startup")
async def on_startup():
    await producer.start()

@app.on_event("shutdown")
async def on_shutdown():
    await producer.stop()

@app.post("/send/{topic}")
async def produce(topic: str, message: str):
    await producer.send_and_wait(topic, message.encode('utf-8'))
    return {"message": "Message sent successfully"}

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
            consumed_messages.append(message)
            print("consumed: ", msg.value.decode('utf-8'))
    finally:
        await consumer.stop()

def start_consumer_task():
    background_tasks = BackgroundTasks()
    background_tasks.add_task(consume)
    return background_tasks

@app.on_event("startup")
async def startup_event():
    start_consumer_task()
    

@app.get("/messages")
def get_messages():
    return {"messages": consumed_messages}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)