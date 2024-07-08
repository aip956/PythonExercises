# Use the official Python image from the Docker Hub
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Upgrade pip to the latest version and install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the app directory into the Docker image
COPY . .

# Make PORT 6000 available to the world outside this container    
EXPOSE 6000

# Define environment variable
# ENV NAME World

# Run the app when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6000"]
