import threading

import __init__
import paho.mqtt.client as client_lib
import time
from sistem_climatizare.senzori_centralizare.basic_sensor import BasicSensor
import sistem_climatizare.setari_utilizator.json_parser as json_parser

temperatura_dorita = float(json_parser.json_read()["Temperatura"])
nr_humans = None


class Hardware(threading.Thread):
    @staticmethod
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

    @staticmethod
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

    def __init__(self, *args, **kwargs):
        super(Hardware, self).__init__(*args, **kwargs)
        broker = "localhost"
        self.subscriber_temp = client_lib.Client("Hardware_Temp")
        self.subscriber_temp.connect(broker)
        self.subscriber_humans = client_lib.Client("Hardware_Humans")
        self.subscriber_humans.connect(broker)
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.is_set()

    def hardware_loop(self):
        while not self.stopped():
            try:
                self.subscriber_temp.loop_start()
                self.subscriber_temp.subscribe(BasicSensor.__name__ + "/Temperature")
                self.subscriber_temp.on_message = self.fnc_activa_temp
                self.subscriber_temp.loop_stop()

                self.subscriber_humans.loop_start()
                self.subscriber_humans.subscribe("HumanSensor")
                self.subscriber_humans.on_message = self.fnc_activa_human
                self.subscriber_humans.loop_stop()

                time.sleep(1)
            except Exception as e:
                print(e)
            except KeyboardInterrupt:
                break
        print("Good Bye!")


if __name__ == "__main__":
    hardware = Hardware()
    hardware.hardware_loop()
