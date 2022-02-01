import threading
from random import randrange

import paho.mqtt.client as mqtt_client
import time


class BasicSensor(threading.Thread):
    def __init__(self, sensor_name, *args, **kwargs):
        super(BasicSensor, self).__init__(*args, **kwargs)

        self.sensor_name = sensor_name
        self.broker = "localhost"
        self.sensor_name = "Senzor_" + sensor_name
        self.topic = "Circulatie/" + sensor_name
        self.publisher = mqtt_client.Client(sensor_name)
        self.publisher.connect(self.broker)
        self._stop = threading.Event()

    def stop(self):
        with threading.Lock():
            self._stop.set()

    def stopped(self):
        with threading.Lock():
            return self._stop.is_set()

    def sensor_loop(self, max_sleep_time):
        while True:
            if self.stopped():
                return
            signal = randrange(2)
            if signal:
                self.publisher.publish(self.topic, time.time())
            time.sleep(randrange(max_sleep_time))
