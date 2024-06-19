Create virtual env:
python3 -m venv venv

Activate 
source venv/bin/activate

Install packages:
pip install fastapi uvicorn psycopg2-binary sqlalchemy pika

Start Rabbit server: docker start rabbitmq
Stop Rabbit server: docker stop rabbitmq


Recompile and build:
docker-compose down --rmi all
docker-compose up --build

Determine which servers are running:
docker ps -a

Check logs to see if rabbit and web servers are running:
docker logs taskmanager-rabbitmq-1
docker logs taskmanager-web-1

With rabbit server running, can go to RabbitMQ ManagementUI:
URL: http://localhost:15673
Username: rabbitmq
Password: local
Check Connections tab; it should shows


kafka you have to add priority, faster
Rabbit includes it
should try to write own priority
run server
download package, bin/startzookeeper server, start kafka server
docker: add api
2 yml files; one for kafka, one for api


