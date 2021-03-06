import os
import datetime
import pathlib


def get_data_curenta():
    current_time = datetime.datetime.now()
    data_curenta = str(current_time).split('.')[0].strip()
    return data_curenta


def get_lista_nume_setari():
    lista_nume_setari = []
    for path in pathlib.Path(path_setari_custom_abs).iterdir():
        nume_fisier = str(os.path.split(path)[-1])
        nume_setare = nume_fisier.split('.')[0]
        lista_nume_setari.append(nume_setare)
    return lista_nume_setari


# Path dinamic

# In acest punct: current_folder = [path_absolut/sistem_climatizare/setari_utilizator]

path_setari_utilizator_abs = os.path.dirname(__file__) + '/'
# In acest punct: current_folder = setari_utilizator
current_folder = path_setari_utilizator_abs.split('\\')[-1]

path_setari_custom_abs = path_setari_utilizator_abs + "setari_custom/"
path_setari_ram_abs = path_setari_utilizator_abs + "ram/"
nume_fisier_ram = "fisier_ram.json"

lista_nume_setari = get_lista_nume_setari()
