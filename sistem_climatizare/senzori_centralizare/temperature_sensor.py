import __init__
import time
from basic_sensor import BasicSensor
import threading
import random


class TemperatureSensor:
    @staticmethod
    def sensor_loop(self: BasicSensor, min_sleep_time, max_sleep_time, **kwargs):
        while True:
            if self.stopped():
                return
            temperatura = round(random.uniform(kwargs['min_temp'], kwargs['max_temp']), 1)
            # Primul argument din functia publish este Topicul
            self.publisher.publish(self.topic, temperatura)
            print("S-a transmis temperatura de " + str(temperatura))
            time.sleep(random.randint(min_sleep_time, max_sleep_time))

    def __init__(self):
        self.sensor_temp = BasicSensor("Temperature")
        self.sensor_temp.sensor_loop = self.sensor_loop
        self.broker = "localhost"
        BasicSensor.init_sensors(20, 60, self.sensor_temp, min_temp=-5, max_temp=35)

    def loop_monitor(self):
        while True:
            try:
                threading.Event().wait()
            except Exception as e:
                print(e)
            except KeyboardInterrupt:
                self.sensor_temp.stop()
                print("Good Bye!")
                break


if __name__ == "__main__":
    temperature_sensor = TemperatureSensor()
    temperature_sensor.loop_monitor()
