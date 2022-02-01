import __init__
import threading
import paho.mqtt.client as mqtt_client
import time
import random
import sistem_climatizare.setari_utilizator.json_parser as json_parser
from sistem_climatizare.senzori_centralizare.basic_sensor import BasicSensor


class HumanSensor:
    @staticmethod
    def sensor_loop(self: BasicSensor, min_sleep_time, max_sleep_time):
        while True:
            if self.stopped():
                return
            self.publisher.publish(self.topic, time.time())
            time.sleep(random.randint(min_sleep_time, max_sleep_time))

    def __init__(self):
        self.sensor_int = BasicSensor("Inside")
        self.sensor_ext = BasicSensor("Outside")
        self.sensor_int.sensor_loop = self.sensor_loop
        self.sensor_ext.sensor_loop = self.sensor_loop
        self.broker = "localhost"
        BasicSensor.init_sensors(0, 5, self.sensor_int, self.sensor_ext)
        self.subscriber_int = mqtt_client.Client(self.sensor_int.sensor_name)
        self.subscriber_int.connect(self.broker)
        self.subscriber_ext = mqtt_client.Client(self.sensor_ext.sensor_name)
        self.subscriber_ext.connect(self.broker)
        self.publisher = mqtt_client.Client(self.__class__.__name__)
        self.publisher.connect(self.broker)
        self.sensor_times = dict()
        self.setari = json_parser.json_read()
        self.lock = threading.Lock()

    def loop_monitor(self):
        def monitor_aux(client, user_data, message):
            message = message.payload.decode("utf-8")
            # print(client, user_data, message)
            with self.lock:
                self.sensor_times[client] = float(message)

        def change_power():
            if len(self.sensor_times) == 2:
                time_sensor_int = self.sensor_times[self.subscriber_int]
                time_sensor_ext = self.sensor_times[self.subscriber_ext]

                if abs(time_sensor_int - time_sensor_ext) < 3.0 and time_sensor_int != time_sensor_ext:
                    self.sensor_times = dict()
                    co_persoane = self.setari["Numar_Persoane"]

                    if time_sensor_ext < time_sensor_int:
                        print("Un om a intrat")
                        co_persoane += 1
                    elif co_persoane > 0:
                        print("Un om a iesit")
                        co_persoane -= 1
                    else:
                        return

                    self.publisher.publish(topic=self.__class__.__name__, payload=co_persoane)
                    self.setari["Numar_Persoane"] = co_persoane
                    json_parser.json_write(self.setari)

        try:
            while True:
                self.subscriber_int.loop_start()
                self.subscriber_int.subscribe(self.sensor_int.topic)
                self.subscriber_int.on_message = monitor_aux
                self.subscriber_int.loop_stop()

                self.subscriber_ext.loop_start()
                self.subscriber_ext.subscribe(self.sensor_ext.topic)
                self.subscriber_ext.on_message = monitor_aux
                self.subscriber_ext.loop_stop()

                with self.lock:
                    change_power()
                time.sleep(1)
        except KeyboardInterrupt:
            self.sensor_int.stop()
            self.sensor_ext.stop()
            print("Good Bye!")


if __name__ == "__main__":
    human_sensor = HumanSensor()
    human_sensor.loop_monitor()
