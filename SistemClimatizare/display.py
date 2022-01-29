import paho.mqtt.client as client_lib
import time

broker = "localhost"
subscriber =  client_lib.Client("Display")

def fnc_activa(client, user_data, message):
  print("Mesaj primit: ", str(message.payload.decode("utf-8")), str(client))



subscriber.connect(broker)

while True:
  subscriber.loop_start()

  subscriber.subscribe("Temperatura")
  subscriber.on_message = fnc_activa


  time.sleep(2)
  subscriber.loop_stop()
