# Use an official Python runtime as the base image
FROM --platform=linux/amd64 python:3.12-slim

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    chromium \
    chromium-driver

WORKDIR /app
ENV PORT=8080

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run the Python application
CMD ["python", "src/main.py"]
