import paho.mqtt.client as client_lib
import time

broker = "localhost"
publisher = client_lib.Client("SenzorCaldura")
publisher.connect(broker)

while True:
    temperatura = 16.0
    # Primul argument din functia publish este Topicul
    publisher.publish("Temperatura", temperatura)
    print("S-a transmis temperatura de " + str(temperatura))
    time.sleep(1)
