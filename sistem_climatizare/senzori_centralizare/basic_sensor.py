import __init__
import threading
import paho.mqtt.client as mqtt_client


class BasicSensor(threading.Thread):
    @classmethod
    def init_sensors(cls, min_response_time, max_response_time, *sensors, **kwargs):
        for sensor in sensors:
            t = threading.Thread(target=sensor.sensor_loop, args=(sensor, min_response_time, max_response_time), kwargs=kwargs)
            t.start()

    def __init__(self, sensor_name, *args, **kwargs):
        super(BasicSensor, self).__init__(*args, **kwargs)
        self.sensor_name = sensor_name
        self.broker = "localhost"
        self.sensor_name = "Sensor_" + sensor_name
        self.topic = self.__class__.__name__ + "/" + sensor_name
        self.publisher = mqtt_client.Client(sensor_name)
        self.publisher.connect(self.broker)
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.is_set()

    def sensor_loop(self, *args, **kwargs):
        pass
