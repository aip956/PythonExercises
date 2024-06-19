Create virtual env:
python3 -m venv venv

Activate 
source venv/bin/activate

Install packages:
pip install fastapi uvicorn psycopg2-binary sqlalchemy pika

Start Rabbit server: docker start rabbitmq
Stop Rabbit server: docker stop rabbitmq




kafka you have to add priority, faster
Rabbit includes it
should try to write own priority
run server
download package, bin/startzookeeper server, start kafka server
docker: add api
2 yml files; one for kafka, one for api


