import paho.mqtt.client as client_lib
from intializare_setari import default_app
from firebase_admin import db
import time


broker = "mqtt.eclipseprojects.io"
subscriber = client_lib.Client("Hardware")
subscriber.connect(broker)
subscriber.subscribe("Temperatura")


root = db.reference()
fisier_initilizare = root.child('FisierInitializare').get()
Temperatura_Dorita = float(fisier_initilizare["Temperatura"])

def fct_test(client, user_data, message):
  print('Ceva')

# subscriber.loop_start()
# subscriber.on_message = fct_test
# subscriber.loop_end()

def fnc_activa(client, user_data, message):
  payload = message.payload.decode("utf-8")
  payload = float(payload)

  if (payload < Temperatura_Dorita):
    print("Marim temperatura!" + str(payload))
  elif (payload > Temperatura_Dorita):
    print("Scadem temperatura!" + str(payload))
  else:
    print("Mentinem temepratura")


while True:
  subscriber.loop_start()
  time.sleep(1)

  subscriber.on_message = fnc_activa

  time.sleep(1)
  subscriber.loop_stop()
