import __init__
import json
import os
import sistem_climatizare.firebase_backup.firebase_api as firebase_api
from sistem_climatizare.setari_utilizator.variables import path_setari_custom_abs


def stergere_setare_fct(nume_setare_custom):
    path_setare = path_setari_custom_abs + "/" + nume_setare_custom
    nume_fisier_setare = path_setare + ".json"

    if os.path.exists(nume_fisier_setare):
        if nume_setare_custom == "setari_default":
            raise Exception("Setarea default nu se sterge")

        os.remove(nume_fisier_setare)
    else:
        raise Exception("Setarea nu exista!")


if __name__ == "__main__":
    while True:
        try:
            nume_setare = input("Stergeti setarea cu numele: ")
            stergere_setare_fct(nume_setare)
        except KeyboardInterrupt:
            print("Canceled!")
            break
        except Exception as e:
            print(e)
        else:
            print("Succes!")
            break
