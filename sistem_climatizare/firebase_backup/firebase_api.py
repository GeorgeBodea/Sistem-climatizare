import os

import __init__
import json
import pyrebase  # update requests and requests-toolbelt or use pip install pyrebase4
import pathlib
from sistem_climatizare.setari_utilizator.variables import path_setari_custom_abs

def __load_json_config():

    with open(os.path.dirname(__file__)+'/apiKey.json', 'r') as f:
        firebase_config = json.loads(f.read())
    return firebase_config


firebase = pyrebase.initialize_app(__load_json_config())


def get_user_auth(email, password):
    auth = firebase.auth()
    auth.sign_in_with_email_and_password(email, password)
    return auth.current_user


def get_user_settings_obj(email, password):
    user = get_user_auth(email, password)
    return firebase.database().child("users").child(user["localId"]), user["idToken"]


def upload_setting(email, password, setare):
    user, token = get_user_settings_obj(email, password)
    user.child(setare["Nume_Setare"]).set(token=token, data=setare)


def delete_setting_no_key(email, password, nume_setare):
    user, token = get_user_settings_obj(email, password)
    settings = get_settings(email, password).val()
    for i in settings:
        if settings[i]['Nume_Setare'] == nume_setare:
            user.child(i).remove(token=token)
            break


def delete_setting_by_key(email, password, nume_setare):
    user, token = get_user_settings_obj(email, password)
    user.child(nume_setare).remove(token=token)


def get_settings(email, password):
    user, token = get_user_settings_obj(email, password)
    db = user.get(token=token)
    return db


def create_new_account(email, password):
    firebase.auth().create_user_with_email_and_password(email=email, password=password)


def upload_all_settings(email, password):
    user, token = get_user_settings_obj(email, password)
    setari = dict()
    for path in pathlib.Path(path_setari_custom_abs).iterdir():
        if path.is_file():
            with open(path, 'r') as f:
                setare = json.loads(f.read())
                setari[setare["Nume_Setare"]] = setare
    user.set(setari, token=token)


def download_all_settings(email, password):
    settings = get_settings(email, password).val()
    for i in settings:
        print(settings[i])
        with open(path_setari_custom_abs + settings[i]["Nume_Setare"] + ".json", 'w') as fisier_setare:
            json.dump(settings[i], fisier_setare, indent=2)
            fisier_setare.write('\n')


if __name__ == "__main__":
    while True:
        try:
            print("Sync Settings!")
            new_email = input("Email: ")
            new_password = input("Password: ")
            opt = input("Alegeti optiune: Upload sau Download: ")
            if opt == "Upload":
                upload_all_settings(new_email, new_password)
            elif opt == "Download":
                download_all_settings(new_email, new_password)
            else:
                raise Exception("Invalid option!")
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            print("Cancelled!")
            break
        else:
            print("Succes!")
            break
