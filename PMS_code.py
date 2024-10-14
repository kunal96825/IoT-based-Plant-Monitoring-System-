import paho.mqtt.client as mqtt
import Adafruit_DHT
import time
import os

# Sensor configurations
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # GPIO pin for DHT22
MOISTURE_PIN = 17  # GPIO pin for soil moisture
LIGHT_PIN = 18  # GPIO pin for light sensor

# MQTT configurations
mqtt_broker = "mqtt.eclipse.org"  # Replace with your broker
mqtt_topic = "plant_monitor"

client = mqtt.Client()
client.connect(mqtt_broker)

while True:
    # Read DHT22 data
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    
    # Read soil moisture
    moisture = os.popen(f"cat /sys/bus/iio/devices/iio:device0/scan_elements/in_voltage{MOISTURE_PIN}_raw").read().strip()
    
    # Read light intensity (for LDR)
    light = os.popen(f"cat /sys/bus/iio/devices/iio:device0/scan_elements/in_voltage{LIGHT_PIN}_raw").read().strip()

    # Publish data
    data = {
        "temperature": temperature,
        "humidity": humidity,
        "moisture": moisture,
        "light": light
    }
    
    client.publish(mqtt_topic, str(data))
    
    # Check conditions and send alerts
    if moisture < threshold_moisture or light < threshold_light:
        client.publish("alerts", "Your plant needs attention!")
        
    time.sleep(60)  # Delay for a minute
