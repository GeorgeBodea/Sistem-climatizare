import __init__
import threading
import time
import paho.mqtt.client as mqtt_client
from sistem_climatizare.senzori_centralizare.basic_sensor import BasicSensor
from sistem_climatizare.senzori_centralizare.temperature_sensor import TemperatureSensor
from sistem_climatizare.senzori_centralizare.human_sensor import HumanSensor

test_passed = None


def test_sensor_outside_exists():
    def my_callback(client, user, data):
        global test_passed
        test_passed = True

    human_sensor = HumanSensor()
    t = threading.Thread(target=human_sensor.loop_monitor)
    t.start()
    global test_passed
    broker = 'localhost'
    subscriber = mqtt_client.Client("test_sensor_outside")
    subscriber.connect(broker)
    test_passed = False

    for i in range(10):
        subscriber.loop_start()
        subscriber.subscribe(BasicSensor.__name__ + "/Outside")
        subscriber.on_message = my_callback
        time.sleep(1)
        subscriber.loop_stop()
        if test_passed:
            break
    assert test_passed is True
    human_sensor.stop()


def test_sensor_inside_exists():
    def my_callback(client, user, data):
        global test_passed
        test_passed = True

    human_sensor = HumanSensor()
    t = threading.Thread(target=human_sensor.loop_monitor)
    t.start()
    global test_passed
    broker = 'localhost'
    subscriber = mqtt_client.Client("test_sensor_inside")
    subscriber.connect(broker)
    test_passed = False

    for i in range(10):
        subscriber.loop_start()
        subscriber.subscribe(BasicSensor.__name__ + "/Inside")
        subscriber.on_message = my_callback
        time.sleep(1)
        subscriber.loop_stop()
        if test_passed:
            break
    assert test_passed is True
    human_sensor.stop()


def test_sensor_temperature_exists():
    def my_callback(client, user, data):
        global test_passed
        test_passed = True

    temperature_sensor = TemperatureSensor(1, 5)
    t = threading.Thread(target=temperature_sensor.loop_monitor)
    t.start()
    global test_passed
    broker = 'localhost'
    subscriber = mqtt_client.Client("test_sensor_temperature")
    subscriber.connect(broker)
    test_passed = False

    for i in range(10):
        subscriber.loop_start()
        subscriber.subscribe(BasicSensor.__name__ + "/Temperature")
        subscriber.on_message = my_callback
        time.sleep(1)
        subscriber.loop_stop()
        if test_passed:
            break
    assert test_passed is True
    temperature_sensor.stop()
