import __init__
import pytest
import time
import requests
import threading
import sistem_climatizare.api_http.app as app_http
import sistem_climatizare.setari_utilizator.alegere_setare as alegere_setare


def test_start_server():
    httpd = app_http.HTTPServer(("", app_http.PORT), app_http.NucleumHTTP)
    t = threading.Thread(target=httpd.serve_forever)
    t.start()
    time.sleep(3)
    response = requests.get('http://localhost:8088/fisiere_custom')
    assert alegere_setare.nr_fisiere() == len(str(response.content).split(';'))

    httpd.shutdown()
