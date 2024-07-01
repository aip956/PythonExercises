# Dockerfile

# official docker image
FROM python:3.11.1-slim

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /app/requirements.txt 
RUN pip install --upgrade pip --no-cache-dir --upgrade -r /app/requirements.txt

# copy project
COPY ./app /app

# run the application
# CMD ["fastapi", "run", "app/main.py", "--port", "80"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]