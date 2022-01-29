import os

# Path dinamic

path_setari_utilizatori_abs = os.path.dirname(__file__)
# In acest punct: current_folder = [path_absolut/SistemClimatizare/setari_utilizatori]


current_folder = path_setari_utilizatori_abs.split('\\')[-1]
# In acest punct: current_folder = setari_utilizatori

path_setari_custom = current_folder + "/setari_custom"
path_setari_ram = path_setari_utilizatori_abs + "/RAM"
