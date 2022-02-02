import __init__
import time
from sistem_climatizare.senzori_centralizare.basic_sensor import BasicSensor
import threading
import random


class TemperatureSensor(threading.Thread):
    @staticmethod
    def sensor_loop(self: BasicSensor, min_sleep_time, max_sleep_time, **kwargs):
        while not self.stopped():
            temperatura = round(random.uniform(kwargs['min_temp'], kwargs['max_temp']), 1)
            # Primul argument din functia publish este Topicul
            self.publisher.publish(self.topic, temperatura)
            print("S-a transmis temperatura de " + str(temperatura))
            time.sleep(random.randint(min_sleep_time, max_sleep_time))

    def __init__(self, min_response_time, max_response_time, *args, **kwargs):
        super(TemperatureSensor, self).__init__(*args, **kwargs)
        self.sensor_temp = BasicSensor("Temperature")
        self.sensor_temp.sensor_loop = self.sensor_loop
        self.broker = "localhost"
        BasicSensor.init_sensors(min_response_time, max_response_time, self.sensor_temp, min_temp=-5, max_temp=35)
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.is_set()

    def loop_monitor(self):
        while not self.stopped():
            try:
                self._stop.wait()
            except Exception as e:
                print(e)
            except KeyboardInterrupt:
                break
        print("Good Bye!")
        self.sensor_temp.stop()


if __name__ == "__main__":
    temperature_sensor = TemperatureSensor(20, 60)
    temperature_sensor.loop_monitor()
