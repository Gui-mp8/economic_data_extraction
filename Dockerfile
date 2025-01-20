# Use an official Python runtime as the base image
FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    chromium \
    chromium-driver

WORKDIR /app
EXPOSE 8000

COPY . .

# ENV GOOGLE_APPLICATION_CREDENTIALS="./suzano-challenge.json"

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# # Run the Python application
# CMD ["python", "src/main.py"]
