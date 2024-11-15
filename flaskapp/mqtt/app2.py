import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties=None):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("testtopic/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

# Create an MQTT client instance
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Set the username and password for MQTT authentication
mqttc.username_pw_set(username="admin", password="admin")

# Assign the callback functions
mqttc.on_connect = on_connect
mqttc.on_message = on_message

# Connect to the MQTT broker
mqttc.connect("10.64.74.89", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
mqttc.loop_forever()
