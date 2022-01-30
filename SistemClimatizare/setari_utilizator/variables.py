import os
import datetime


def get_data_curenta():
    current_time = datetime.datetime.now()
    data_curenta = str(current_time).split('.')[0].strip()
    return data_curenta


# Path dinamic

path_setari_utilizator_abs = os.path.dirname(__file__)
# In acest punct: current_folder = [path_absolut/SistemClimatizare/setari_utilizator]


current_folder = path_setari_utilizator_abs.split('\\')[-1]
# In acest punct: current_folder = setari_utilizator

path_setari_custom_abs = path_setari_utilizator_abs + "/setari_custom"
path_setari_ram_abs = path_setari_utilizator_abs + "/RAM"
nume_fisier_ram = "/fisier_ram.json"