import __init__
import paho.mqtt.client as client_lib
import time
from sistem_climatizare.senzori_centralizare.basic_sensor import BasicSensor


def fnc_activa(client, user_data, message):
    print("Temperatura primita: ", str(message.payload.decode("utf-8")))


if __name__ == "__main__":
    broker = "localhost"
    subscriber = client_lib.Client("Display")
    subscriber.connect(broker)

    try:
        while True:
            subscriber.loop_start()

            subscriber.subscribe(BasicSensor.__name__ + "/Temperature")
            subscriber.on_message = fnc_activa

            time.sleep(2)
            subscriber.loop_stop()
    except KeyboardInterrupt:
        print("Good Bye!")
