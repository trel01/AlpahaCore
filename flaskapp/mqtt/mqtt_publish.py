import paho.mqtt.client as mqtt
import time
from datetime import datetime

# Callback function for when the client receives a CONNACK response
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to a topic (optional, you can remove if only sending data)
    client.subscribe("testtopic/#")

# Callback function for when a PUBLISH message is received
def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {str(msg.payload.decode('utf-8'))}")

# Create MQTT client instance
mqttc = mqtt.Client()  # Use default protocol (works with v3.1.1 and v5)

# Assign callback functions
mqttc.on_connect = on_connect
mqttc.on_message = on_message



# Enable logger for debugging (optional)
mqttc.enable_logger()

# Try to connect to the broker
try:
    mqttc.connect("localhost", 1883, keepalive=60)  # ใช้ localhost แทน host.docker.internal
except Exception as e:
    print(f"Failed to connect: {e}")

# Create message payload with current time
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get current time in the format YYYY-MM-DD HH:MM:SS
message = f"Hello from client at {current_time}"

# Publish a message to the topic "testtopic/testmessage" with time included
mqttc.publish("testtopic/testmessage", payload=message, qos=1)

# Start the network loop to handle incoming messages and reconnect if necessary
try:
    mqttc.loop_start()  # ใช้ loop_start() แทน loop_forever() เพื่อให้โปรแกรมไม่ถูกหยุด
    # ทำให้รอ 5 วินาทีเพื่อให้ client ส่งข้อความ
    time.sleep(5)  # ทำให้รอ 5 วินาทีเพื่อให้ client ส่งข้อความ
except KeyboardInterrupt:
    print("Disconnected")
    mqttc.disconnect()
    mqttc.loop_stop()
