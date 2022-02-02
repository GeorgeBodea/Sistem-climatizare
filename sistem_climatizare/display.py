import threading

import __init__
import paho.mqtt.client as client_lib
import time
from sistem_climatizare.senzori_centralizare.basic_sensor import BasicSensor


class Display(threading.Thread):
    @staticmethod
    def fnc_activa(client, user_data, message):
        print("Temperatura primita: ", str(message.payload.decode("utf-8")))

    def __init__(self, *args, **kwargs):
        super(Display, self).__init__(*args, **kwargs)
        broker = "localhost"
        self.subscriber = client_lib.Client("Display")
        self.subscriber.connect(broker)
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.is_set()

    def display_loop(self):
        while not self.stopped():
            try:
                self.subscriber.loop_start()
                self.subscriber.subscribe(BasicSensor.__name__ + "/Temperature")
                self.subscriber.on_message = self.fnc_activa
                self.subscriber.loop_stop()
                time.sleep(1)
            except Exception as e:
                print(e)
            except KeyboardInterrupt:
                break
        print("Good Bye!")


if __name__ == "__main__":
    display = Display()
    display.display_loop()
