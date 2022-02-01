import json
import os
import sistem_climatizare.firebase_backup.firebase_api as firebase_api
from variables import path_setari_custom_abs

if __name__ == "__main__":
    while True:
        try:
            nume_setare_custom = input("Stergeti setarea cu numele: ")
            path_setare = path_setari_custom_abs + "/" + nume_setare_custom
            nume_fisier_setare = path_setare + ".json"

            if os.path.exists(nume_fisier_setare):
                if nume_setare_custom == "setari_default":
                    raise Exception("Setarea default nu se sterge")

                with open(nume_fisier_setare, 'r') as f:
                    email = json.loads(f.read())["Email"]
                    password = input("Password for {}: ".format(email))
                firebase_api.delete_setting_by_key(email=email, password=password, nume_setare=nume_setare_custom)
                os.remove(nume_fisier_setare)
            else:
                raise Exception("Setarea nu exista!")
        except KeyboardInterrupt:
            print("Canceled!")
            break
        except Exception as e:
            print(e)
        else:
            print("Succes!")
            break
