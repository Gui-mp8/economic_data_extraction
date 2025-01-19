#!/bin/bash

# Run Selenium server in the background
java -jar jars/selenium-server-4.27.0.jar standalone &

# Run the Python application
python3 src/main.py
