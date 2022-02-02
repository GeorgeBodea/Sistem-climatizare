import __init__
from input_output_helper import get_display_output, set_keyboard_input
import pytest
import pathlib
import runpy
import sistem_climatizare.api_http.app as app
from sistem_climatizare.setari_utilizator.variables import path_setari_custom_abs, get_data_curenta, path_setari_ram_abs, nume_fisier_ram
import json
import os

# def test_extrage_fisier(fisier_extras):