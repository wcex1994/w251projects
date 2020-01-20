import paho.mqtt.client as mqtt
import time

#Reference: https://www.ev3dev.org/docs/tutorials/sending-and-receiving-messages-with-mqtt/
# Define constant
REMOTE_MQTT_TOPIC = "hw03cloud"
CLOUD_ADDR = "158.85.94.38"
REMOTE_PORT = 1883

LOCAL_MQTT_TOPIC = "hw03new"
LOCAL_ADDR = "172.18.0.2"


# Define function for each message the local client received, send it to the cloud client.
#print("message received is:",str(msg.payload.decode('utf-8')))

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)

def on_connect_remote(client, userdata, flags, rc):
        print("connected to remote broker with rc: " + str(rc))


def on_message(client,userdata, msg):
  try:
    print("message received!")
    # if we wanted to re-publish this message, something like this should work
    print("message received is:",str(len(msg.payload)))
    global REMOTE_MQTT_TOPIC
    global client_cloud
    msg = msg.payload
    client_cloud.publish(REMOTE_MQTT_TOPIC, payload=msg)
    print("message sent!")
  except:
    print("Unexpected error:", sys.exc_info()[0])

# IBM VM mosquitto broker
client_cloud = mqtt.Client("cloudsubscriber")
client_cloud.on_connect = on_connect_remote
client_cloud.connect(CLOUD_ADDR,REMOTE_PORT)

# Jetson mosquitto broker
client_local = mqtt.Client("localforwarder")
client_local.on_connect = on_connect_local
client_local.connect(LOCAL_ADDR,1883, 60)
client_local.on_message = on_message

# Will have concurrency error if there is no wait in-between
#time.sleep(5)

client_local.loop_forever()
