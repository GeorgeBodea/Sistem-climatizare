import json
import pyrebase  # update requests and requests-toolbelt


def __load_json_config():
    with open('../firebase_backup/apiKey.json', 'r') as f:
        firebase_config = json.loads(f.read())
    return firebase_config


firebase = pyrebase.initialize_app(__load_json_config())
test_email_password = ("qwerty@yahoo.com", "password")


def get_user_auth(email, password):
    auth = firebase.auth()
    auth.sign_in_with_email_and_password(email, password)
    return auth.current_user


def get_user_settings_obj(email, password):
    user = get_user_auth(email, password)
    return firebase.database().child("users").child(user["localId"]), user["idToken"]


def backup_setting(email, password, setare):
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


if __name__ == "__main__":
    while True:
        try:
            print("Create new user!")
            new_email = input("Email: ")
            new_password = input("Password: ")
            create_new_account(new_email, new_password)
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            print("Cancelled!")
            break
        else:
            print("Succes!")
            break
