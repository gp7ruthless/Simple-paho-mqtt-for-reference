import paho.mqtt.client as mqtt #import the client1
import time


def on_message(client, userdata, message):
    print("Msg : " ,str(message.payload.decode("utf-8")), "| Topic : ",message.topic, end = "\n\n")
    #rint("message qos=",message.qos)
    #print("message retain flag=",message.retain)


client = mqtt.Client("client_sub") 
client.on_message=on_message
client.connect("localhost", 9001)

client.subscribe("mytopic")

client.loop_forever() #start the loop