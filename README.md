# IoT-based-Plant-Monitoring-System-

Here's a detailed overview of how to create an IoT-based Plant Monitoring System using a Raspberry Pi. This project involves using sensors to monitor soil moisture, light intensity, and temperature, along with sending alerts to your smartphone.

Project Overview
Objective: To monitor the health of plants by measuring soil moisture, light intensity, and temperature, and sending alerts to a smartphone when the plants require water or more light.

Components Required
Hardware:

Raspberry Pi (any model with GPIO pins)
Soil moisture sensor
Light sensor (e.g., LDR or BH1750)
Temperature sensor (e.g., DHT11 or DHT22)
Breadboard and jumper wires
Resistors (if needed)
Wi-Fi dongle (if using a Raspberry Pi without built-in Wi-Fi)
Power supply for Raspberry Pi
Software:

Raspbian OS (or any preferred OS for Raspberry Pi)
Python (for programming the sensors)
MQTT broker (e.g., Mosquitto) for communication
Flask (for web server, if needed)
Blynk or similar mobile app for alerts and monitoring
Steps to Build the System
Step 1: Set Up the Raspberry Pi
Install Raspbian OS: Download and install Raspbian OS on your Raspberry Pi.
Connect to Wi-Fi: Ensure your Raspberry Pi is connected to the internet.
Step 2: Connect the Sensors
Soil Moisture Sensor: Connect the sensor's VCC and GND to Raspberry Pi’s 3.3V and GND. Connect the signal pin to one of the GPIO pins (e.g., GPIO17).
Light Sensor: If using an LDR, connect it in a voltage divider configuration with a resistor and connect the output to a GPIO pin. For the BH1750, connect it via I2C (SDA to SDA, SCL to SCL).
Temperature Sensor: Connect the DHT11/DHT22 sensor's VCC and GND to Raspberry Pi’s 3.3V and GND. Connect the signal pin to a GPIO pin (e.g., GPIO27).
Step 3: Install Required Libraries
Use the following commands to install the necessary Python libraries:

sudo apt-get update
sudo apt-get install python3-pip
pip3 install paho-mqtt
pip3 install Adafruit_DHT

Step 4: Write the Python Script
Create a Python script that reads data from the sensors and publishes it to an MQTT broker. Here's a simple example:

python code----------------------------xxxxxxxxxxxxxxxxxxxxxxxx

Step 5: Set Up the MQTT Broker
You can use a public broker like Eclipse Mosquitto or set up your own on the Raspberry Pi. If using Mosquitto, install it with:

sudo apt-get install mosquitto mosquitto-clients

Step 6: Mobile App Integration
Blynk App: Use the Blynk app to create a mobile dashboard for monitoring. Set up the app to receive MQTT messages and display the sensor data.
Configure Alerts: Set up notifications in the app to alert you when the plant needs water or more light.
Step 7: Testing and Calibration
Test the System: Ensure all sensors are working correctly and the data is being published to the MQTT broker.
Calibrate Thresholds: Adjust moisture and light thresholds based on the specific needs of your plants.
Optional Enhancements
Data Logging: Store the sensor data in a database (like SQLite) for historical analysis.
Web Dashboard: Create a Flask web application to visualize real-time data.
User Authentication: Secure the dashboard and mobile app with user authentication.
Additional Sensors: Add more sensors, such as pH sensors or nutrient sensors, for comprehensive monitoring.
This IoT-based Plant Monitoring System will allow you to keep your plants healthy and well-cared for by providing real-time data and alerts. Let me know if you need help with specific parts of the project!
