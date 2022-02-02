import __init__
from input_output_helper import get_display_output, set_keyboard_input
import pytest
import pathlib
import runpy
import sistem_climatizare.setari_utilizator.adauga_setare as adauga_setare
import sistem_climatizare.setari_utilizator.alegere_setare as  alegere_setare
import sistem_climatizare.setari_utilizator.stergere_setare as stergere_setare
from sistem_climatizare.setari_utilizator.variables import path_setari_custom_abs, get_data_curenta, path_setari_ram_abs, nume_fisier_ram
import sistem_climatizare.senzori_centralizare.temperature_sensor as temperature_sensor
import sistem_climatizare.senzori_centralizare.temperature_sensor as basic_sensor
import json
import os

# def test_instantiate_temperature_sensor():
#     temperature_sensor = temperature_sensor.TemperatureSensor()
