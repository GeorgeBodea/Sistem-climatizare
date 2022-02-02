import __init__
import pytest
import sistem_climatizare.firebase_backup.firebase_api as firebase_api
import random
import sistem_climatizare.setari_utilizator.variables as variables

email = "tester@sisteme-climatizare.ro"
password = "tester"


@pytest.fixture(scope="session", autouse=True)
def create_account():
    try:
        firebase_api.create_new_account(email, password)
    except Exception as e:
        pass


def test_sync_settings():
    test_setting = dict()
    test_setting["Data_Creare"] = variables.get_data_curenta()
    test_setting["Numar_Persoane"] = random.randint(1, 10)
    test_setting["Nume_Setare"] = "test"
    test_setting["Temperatura"] = round(random.uniform(-5, 35), 1)

    firebase_api.upload_setting(email, password, setare=test_setting)

    cloud_setting = firebase_api.get_settings(email, password)

    test_passed = False
    for i in cloud_setting.val():
        if test_setting == dict(cloud_setting.val()[i]):
            test_passed = True
            break
    assert test_passed
