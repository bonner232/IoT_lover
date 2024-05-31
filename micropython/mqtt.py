import network
import time
from umqtt.simple import MQTTClient
import uasyncio
import neopixel

BROKER_ADDRESS="******"
CLIENT_ID="esp32"
TOPIC_PUBLISH = b'*****'
TOPIC_SUBSCRIBE = b'*****'



def connect_mqtt():
    global client
    try:
        client = MQTTClient(CLIENT_ID, BROKER_ADDRESS)
        client.set_callback(mqtt_callback)
        client.connect()
        
    except Exception as e:
        print("Error:", e)
    
def publish_to_mqtt():
    client.publish(TOPIC_PUBLISH, "1")
    print("pub")


def mqtt_callback(topic, msg):

    print("Received message on topic:", topic)
    print("Message:", msg)
    for i in range(num_pixels):
            pixels[i] = (255, 0, 0)
            pixels.write()
            sleep(1)
            for i in range(num_pixels):
                pixels[i] = (0, 0, 0)
                pixels.write()
    

def read_mqtt():
    global read_var
    client.subscribe(b'test/topic')
    
    client.check_msg()#--> goes to the call back and display msg there
    print("in mqqt")
    await uasyncio.sleep(1)
    
    
    

    





