import __init__
import paho.mqtt.client as client_lib
import time
from sistem_climatizare.senzori_centralizare.basic_sensor import BasicSensor
from sistem_climatizare.senzori_centralizare.human_sensor import HumanSensor
import sistem_climatizare.setari_utilizator.json_parser as json_parser

temperatura_dorita = json_parser.json_read()["Temperatura"]
nr_humans = None


def fnc_activa_temp(client, user_data, message):
    global temperatura_dorita
    payload = message.payload.decode("utf-8")
    payload = float(payload)

    if payload < temperatura_dorita:
        print("Marim temperatura de la {} la {}".format(str(payload), temperatura_dorita))
    elif payload > temperatura_dorita:
        print("Scadem temperatura de la {} la {}".format(str(payload), temperatura_dorita))
    else:
        print("Mentinem temperatura")


def fnc_activa_human(client, user_data, message):
    global nr_humans
    payload = int(message.payload.decode("utf-8"))

    if nr_humans is not None:
        if payload < nr_humans:
            print("A scazut nr de persoane la {}. Crestem puterea!".format(str(payload)))
        elif payload > nr_humans:
            print("A crescut nr de persoane la {}. Scadem puterea!".format(str(payload)))
        else:
            print("Mentinem temepratura")
    nr_humans = payload


if __name__ == "__main__":
    broker = "localhost"
    subscriber_temp = client_lib.Client("Hardware_Temp")
    subscriber_temp.connect(broker)
    subscriber_humans = client_lib.Client("Hardware_Humans")
    subscriber_humans.connect(broker)
    try:
        while True:
            subscriber_temp.loop_start()
            subscriber_temp.subscribe(BasicSensor.__name__ + "/Temperature")
            subscriber_temp.on_message = fnc_activa_temp
            subscriber_temp.loop_stop()

            subscriber_humans.loop_start()
            subscriber_humans.subscribe("HumanSensor")
            subscriber_humans.on_message = fnc_activa_human
            subscriber_humans.loop_stop()

            time.sleep(1)
    except KeyboardInterrupt:
        print("Good Bye!")
