from basicSensor import BasicSensor
import paho.mqtt.client as mqtt_client
import threading
import time
import parsare_setari_senzori


class HumanSensor:

    @classmethod
    def init_sensors(cls, max_response_time, *sensors):
        for sensor in sensors:
            t = threading.Thread(target=sensor.sensor_loop, args=(max_response_time,))
            t.start()

    def __init__(self):
        self.sensor_int = BasicSensor("Interior")
        self.sensor_ext = BasicSensor("Exterior")
        self.broker = "localhost"
        self.__class__.init_sensors(5, self.sensor_int, self.sensor_ext)
        self.subscriber_int = mqtt_client.Client(self.sensor_int.sensor_name)
        self.subscriber_int.connect(self.broker)
        self.subscriber_ext = mqtt_client.Client(self.sensor_ext.sensor_name)
        self.subscriber_ext.connect(self.broker)
        self.sensor_times = dict()
        self.setari = parsare_setari_senzori.parsare_citire()

    def loop_monitor(self):
        def monitor_aux(client, user_data, message):
            message = message.payload.decode("utf-8")
            # print(client, user_data, message)
            self.sensor_times[client] = float(message)

        def change_power():
            if len(self.sensor_times) == 2:
                time_sensor_int = self.sensor_times[self.subscriber_int]
                time_sensor_ext = self.sensor_times[self.subscriber_ext]
                if abs(time_sensor_int - time_sensor_ext) < 3.0:
                    co_persoane = self.setari["Numar_Persoane"]
                    if time_sensor_int < time_sensor_ext:
                        if co_persoane > 0:
                            print("Un om a iesit")
                            co_persoane -= 1
                            self.setari["Numar_Persoane"] = co_persoane
                            parsare_setari_senzori.scriere_setare(self.setari)
                    elif time_sensor_ext < time_sensor_int:
                        print("Un om a intrat")
                        co_persoane += 1
                        self.setari["Numar_Persoane"] = co_persoane
                        parsare_setari_senzori.scriere_setare(self.setari)

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

                change_power()
                time.sleep(1)
        except KeyboardInterrupt:
            self.sensor_int.stop()
            self.sensor_ext.stop()
            print("Good Bye!")


if __name__ == "__main__":
    human_sensor = HumanSensor()
    human_sensor.loop_monitor()
