import __init__
import pytest
import json
import random
import sistem_climatizare.setari_utilizator.variables as variables
import sistem_climatizare.firebase_backup.firebase_api as firebase_api

email = "tester@sisteme-climatizare.ro"
password = "tester"
test_setting = dict()
test_setting["Data_Creare"] = variables.get_data_curenta()
test_setting["Numar_Persoane"] = random.randint(1, 10)
test_setting["Nume_Setare"] = "test"
test_setting["Temperatura"] = round(random.uniform(-5, 35), 1)


def test_create_user():
    try:
        firebase_api.create_new_account(email, password)
    except Exception as e:
        e = str(e)
        # print(e[e.find('{')+1])
        js = json.loads(e[e.find('{'):])
        assert js['error']['message'] == 'EMAIL_EXISTS'


def test_upload_settings():
    firebase_api.upload_setting(email, password, setare=test_setting)

    cloud_setting = firebase_api.get_settings(email, password)

    test_passed = False
    for i in cloud_setting.val():
        if test_setting == dict(cloud_setting.val()[i]):
            test_passed = True
            break
    assert test_passed


def test_delete_setting_no_key(nume_setare="setare_inexistenta"):
    def exista_setarea(email, password, nume_setare):
        user, token = firebase_api.get_user_settings_obj(email, password)

        settings = firebase_api.get_settings(email, password).val()
        for i in settings:
            if settings[i]['Nume_Setare'] == nume_setare:
                return True
        return False

    def json_setare_nu_exista(setare):
        setari = variables.lista_nume_setari

        for json_name in setari:
            print(json_name + ' si ' + json_name[:-5])
            if json_name[:-5] == setare:
                return False

        return True

    firebase_api.delete_setting_no_key(email, password, nume_setare)

    assert (not exista_setarea(email, password, nume_setare)) and json_setare_nu_exista(nume_setare)


def test_delete_setting_by_key():
    firebase_api.upload_setting(email, password, test_setting)
    firebase_api.delete_setting_by_key(email, password, test_setting["Nume_Setare"])


def test_sync_settings():
    firebase_api.upload_setting(email, password, setare=test_setting)
    firebase_api.upload_all_settings(email, password)

    cloud_setting = firebase_api.get_settings(email, password)
    test_passed = True
    for i in cloud_setting.val():
        if i == test_setting["Nume_Setare"]:
            test_passed = False
            break
    assert test_passed


def test_get_user_auth():
    assert firebase_api.get_user_auth(email, password) is not None


def test_load_json_config():
    assert firebase_api.__load_json_config() is not None


def test_get_user_settings_obj():
    user, token = firebase_api.get_user_settings_obj(email, password)
    assert user is not None
    assert token is not None and token != ""


def test_download_all_settings():
    firebase_api.download_all_settings(email, password)
