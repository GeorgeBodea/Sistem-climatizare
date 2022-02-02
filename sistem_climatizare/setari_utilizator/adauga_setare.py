import __init__
import json
from sistem_climatizare.setari_utilizator.variables import path_setari_custom_abs, get_data_curenta


def adaugare_setare_fct(nume_setare_custom, temperatura_dorita, numar_persoane):
    if nume_setare_custom == "Default":
        raise ValueError
    else:
        nume_fisier = path_setari_custom_abs + nume_setare_custom

        setari = dict()
        setari["Nume_Setare"] = nume_setare_custom
        setari["Numar_Persoane"] = numar_persoane
        setari["Temperatura"] = temperatura_dorita
        setari["Data_Creare"] = get_data_curenta()

        with open(nume_fisier + ".json", "w") as f:
            json.dump(setari, f, indent=2)
            f.write('\n')
