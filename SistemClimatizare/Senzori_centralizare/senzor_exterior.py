import paho.mqtt.client as client_lib
import sys 
from random import randrange
import time

broker = "localhost"
publisher = client_lib.Client("SenzorExterior")
publisher.connect(broker)


for semnal in sys.stdin:
  publisher.publish("Circulatie/Exterior", semnal)
  
