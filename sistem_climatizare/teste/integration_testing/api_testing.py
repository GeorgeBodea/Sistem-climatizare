import __init__
import sys
import time

import __init__
from sistem_climatizare.teste.input_output_helper import get_display_output, set_keyboard_input
import pytest
import pathlib
import runpy
import sistem_climatizare.api_http.app as app
from sistem_climatizare.setari_utilizator.variables import path_setari_custom_abs, get_data_curenta, path_setari_ram_abs, nume_fisier_ram
import json
import os
import threading
import sistem_climatizare.api_http.app as app_http
import requests
import pycurl
# @pytest.fixture(autouse=True)
# def run_around_tests():
#     # Code that will run before your test, for example:
#     files_before = # ... do something to check the existing files
#     # A test function will be run at this point
#     yield
#     # Code that will run after your test, for example:
#     files_after = # ... do something to check the existing files
#     assert files_before == files_after
import sistem_climatizare.setari_utilizator.alegere_setare as alegere_setare


# @pytest.fixture(scope="session", autouse=True)
# def start_http_server():
#     # prepare something ahead of all tests
#     t = threading.Thread(target=app_http.start_server)
#     t.start()
#     time.sleep(3)
#

def test_start_server():
    httpd = app_http.HTTPServer(("", app_http.PORT), app_http.NucleumHTTP)
    t = threading.Thread(target=httpd.serve_forever)
    t.start()
    time.sleep(3)
    response = requests.get('http://localhost:8088/fisiere_custom')
    assert alegere_setare.nr_fisiere() == len(str(response.content).split(';'))

    httpd.shutdown()



    # app_http.HTTPServer.shutdown()
