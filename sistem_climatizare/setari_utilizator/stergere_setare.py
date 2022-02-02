import __init__
import os
from sistem_climatizare.setari_utilizator.variables import path_setari_custom_abs


def stergere_setare_fct(nume_setare_custom):
    path_setare = path_setari_custom_abs + nume_setare_custom
    nume_fisier_setare = path_setare + ".json"

    if os.path.exists(nume_fisier_setare):
        if nume_setare_custom == "Default":
            raise ValueError("Setarea default nu se sterge")

        os.remove(nume_fisier_setare)
    else:
        raise FileNotFoundError("Setarea nu exista!")
