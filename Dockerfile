# Use an official Python runtime as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app
EXPOSE 8080
EXPOSE 4444
# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the current directory to the container
COPY . .

# Run the Python application
CMD ["python", "src/main.py"]
