import paho.mqtt.client as client_lib
import sys
from random import randrange
import time

broker = "mqtt.eclipseprojects.io"
publisher = client_lib.Client("SenzorInterior")
publisher.connect(broker)

for semnal in sys.stdin:
  publisher.publish("Circulatie/Interior", semnal)

