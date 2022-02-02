import __init__
import pytest
import json
import requests
import threading
import sistem_climatizare.api_http.app as app_http
import sistem_climatizare.setari_utilizator.alegere_setare as alegere_setare
from sistem_climatizare.setari_utilizator.variables import path_setari_custom_abs

httpd = app_http.HTTPServer(("", app_http.PORT), app_http.NucleumHTTP)
t = threading.Thread(target=httpd.serve_forever)


def test_start_server():
    t.start()


def test_lista_fisiere_custom():
    response = requests.get('http://localhost:8088/fisiere_custom')
    assert alegere_setare.nr_fisiere() == len(str(response.content).split(';'))


def test_detalii_fisier():
    response = requests.get('http://localhost:8088/fisiere_custom/Default')
    message = str(response.content)

    with open(path_setari_custom_abs + "Default.json", "r") as fisier_setare:
        setting = json.loads(fisier_setare.read())
        for key in setting:
            assert message.find(str(setting[key])) - 1


def test_conexiune_fisiere_custom():
    response = requests.get('http://localhost:8088/fisiere_custom')
    assert response.status_code == 200


def test_conexiune_continut_fisier():
    response = requests.get('http://localhost:8088/fisiere_custom/Default')
    assert response.status_code == 200


def test_conexiune_adaugare_setare():
    response = requests.get('http://localhost:8088/adaugare_setare')
    assert response.status_code == 200


def test_conexiune_stergere_setare():
    response = requests.get('http://localhost:8088/stergere_setare')
    assert response.status_code == 200


def test_conexiune_alegere_setare():
    response = requests.get('http://localhost:8088/alegere_setare')
    assert response.status_code == 200


def test_conexiune_backup_download():
    response = requests.get('http://localhost:8088/backup_download')
    assert response.status_code == 200


def test_conexiune_backup_upload():
    response = requests.get('http://localhost:8088/backup_upload')
    assert response.status_code == 200


def test_conexiune_path_incorect():
    test_passed = False
    try:
        response = requests.get('http://localhost:8088/incorect_route')
    except Exception:
        test_passed = True
    finally:
        assert test_passed


def test_shutdown_server():
    httpd.shutdown()
    t.join()
