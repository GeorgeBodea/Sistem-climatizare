import paho.mqtt.client as client_lib
import time

if __name__ == "__main__":
    broker = "localhost"
    publisher = client_lib.Client("SenzorCaldura")
    publisher.connect(broker)

    try:
        while True:
            temperatura = 16.0
            # Primul argument din functia publish este Topicul
            publisher.publish("Temperatura", temperatura)
            print("S-a transmis temperatura de " + str(temperatura))
            time.sleep(1)
    except KeyboardInterrupt:
        print("Good Bye!")
