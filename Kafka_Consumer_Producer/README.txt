To run:
cd into Kafka_Consumer_Producer

In terminal:
Start/build the container:
docker-compose up -d
Start the app:
uvicorn main:app --reload

Access FastAPI Swagger:
http://127.0.0.1:8000/docs
http://localhost:8000/docs

Post a message:
topic: my_topic
message: Hello Kafka!
Should return code 200


Get the consumed messages:
Get, execute
{
  "messages": [
    {
      "topic": "my_topic",
      "message": "Hello Kafka!"
    }
  ]
}

Stop process in foreground:
Control-C 
Gracefully shut down:
docker-compose stop
Remove containers:
docker-compose down


Make a branch
Commit
