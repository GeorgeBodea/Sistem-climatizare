from random import randrange
import paho.mqtt.client as mqtt_client
import time


class BasicSensor:
    def __init__(self, sensor_name):
        super().__init__()

        self.sensor_name = sensor_name
        self.broker = "localhost"
        self.sensor_name = "Senzor_" + sensor_name
        self.topic = "Circulatie/" + sensor_name
        self.publisher = mqtt_client.Client(sensor_name)
        self.publisher.connect(self.broker)

    def sensor_loop(self, max_sleep_time):
        while True:
            signal = randrange(2)
            if signal:
                self.publisher.publish(self.topic, time.time())
            time.sleep(randrange(max_sleep_time))
