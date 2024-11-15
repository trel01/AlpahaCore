import paho.mqtt.client as mqtt

# Callback function for when the client receives a message
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

# Callback function for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to a specific topic
    client.subscribe("test/topic")  # Topic ที่ต้องการรับ

# Create MQTT client instance
mqttc = mqtt.Client()

# Assign callback functions
mqttc.on_connect = on_connect
mqttc.on_message = on_message

# Set the username and password for authentication if needed
mqttc.username_pw_set("tle", "483312")

# Connect to the MQTT broker (ที่มี IP หรือ host ชื่อที่ใช้)
mqttc.connect("172.17.0.1", 1883, keepalive=60)


# Start the network loop to listen for messages
mqttc.loop_forever()
