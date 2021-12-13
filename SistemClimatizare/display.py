import paho.mqtt.client as client_lib
import time

broker = "mqtt.eclipseprojects.io"
subscriber =  client_lib.Client("Display")

def fnc_activa(client, user_data, message):
  print("Mesaj primit: ", str(message.payload.decode("utf-8")), str(client))



subscriber.connect(broker)

subscriber.loop_start()

subscriber.subscribe("Temperatura")
subscriber.on_message = fnc_activa


time.sleep(30)

