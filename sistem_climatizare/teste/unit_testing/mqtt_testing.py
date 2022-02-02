import __init__
import unittest
import paho.mqtt.client as mqtt
from sistem_climatizare.teste.input_output_helper import get_display_output, set_keyboard_input
import pytest
import pathlib
import runpy
import sistem_climatizare.hardware as hardware
from sistem_climatizare.setari_utilizator.variables import path_setari_custom_abs, get_data_curenta, path_setari_ram_abs, nume_fisier_ram
from sistem_climatizare.senzori_centralizare import temperature_sensor
from sistem_climatizare.senzori_centralizare import basic_sensor
import sistem_climatizare.setari_utilizator.json_parser as json_parser
import json
import os
import time


class TestBrokerConnection(unittest.TestCase):
    def setUp(self):
        self.client = mqtt.Client("Test Client")
        self.client.on_connect = self.on_connect
        self.broker = "localhost"
        self.port = 1883
        self.has_connected = False

    def on_connect(self, client, userdata, flags, rc):  # connect function
        if rc == 0:
            self.has_connected = True

    def test_connection(self):  # test to check connection to broker
        self.client.connect(self.broker, self.port)
        self.client.loop_start()
        time.sleep(2)
        self.client.loop_stop()
        self.assertTrue(self.has_connected)


if __name__ == '__main__':
    unittest.main()
