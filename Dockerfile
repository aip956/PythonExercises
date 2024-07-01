# Ubuntu Docker Image with Python 3.8
FROM ubuntu:20.04

# Set work directory
WORKDIR /code

# Install Python 3 and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install virtualenv
RUN pip3 install --no-cache-dir virtualenv

# Create a virtual environment in the /venv directory
RUN virtualenv /venv

# Install dependencies
COPY requirements.txt /code/requirements.txt
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY app /code/app

# Command to run your application
CMD ["python3", "/code/app/your_script.py"]
