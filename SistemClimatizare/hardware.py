import paho.mqtt.client as client_lib
import time

broker = "localhost"
subscriber = client_lib.Client("Hardware")
subscriber.connect(broker)

Temperatura_Dorita = 15.0


def fct_test(client, user_data, message):
    print('Ceva')


def fnc_activa(client, user_data, message):
    payload = message.payload.decode("utf-8")
    payload = float(payload)

    if payload < Temperatura_Dorita:
        print("Marim temperatura! " + str(payload))
    elif payload > Temperatura_Dorita:
        print("Scadem temperatura! " + str(payload))
    else:
        print("Mentinem temepratura")


while True:
    subscriber.loop_start()

    subscriber.subscribe("Temperatura")
    subscriber.on_message = fnc_activa

    time.sleep(2)
    subscriber.loop_stop()
