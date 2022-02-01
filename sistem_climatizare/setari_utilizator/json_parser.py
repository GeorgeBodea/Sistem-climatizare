import __init__
import json
import sistem_climatizare.setari_utilizator.variables as variables


def json_read(path_fisier=variables.path_setari_ram_abs + variables.nume_fisier_ram):
    with open(path_fisier, "r") as fisier_setare:
        setari = json.loads(fisier_setare.read())
    return setari


def json_write(setari, path_fisier=variables.path_setari_ram_abs + variables.nume_fisier_ram):
    setari["Data_Creare"] = variables.get_data_curenta()
    with open(path_fisier, "w") as fisier_setare:
        json.dump(setari, fisier_setare, indent=2)
        fisier_setare.write('\n')
