import paho.mqtt.client as mqtt
import time
import json

client = mqtt.Client("client_pub")
client.connect("localhost", port=9001)

i = 0
j = 1000
payload = {
    "key1" : i,
    "key2" : j
}

while(1):
    client.publish("mytopic", json.dumps(payload))
    print(f"Published : {payload}")
    
    i += 1
    j -= 1

    payload = {
    "key1" : i,
    "key2" : j
    }   

    time.sleep(5)