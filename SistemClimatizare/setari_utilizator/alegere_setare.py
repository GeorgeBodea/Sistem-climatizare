import pathlib
import shutil
import os
from variables import path_setari_custom, path_setari_ram, path_setari_utilizatori_abs

initial_count = 0
for path in pathlib.Path(path_setari_custom).iterdir():
    if path.is_file():
        # print(path)
        initial_count += 1

print(initial_count)

# La recopiere se suprascrie fisierul din folderul RAM, ceea ce e ne dorim


nume_setare_aleasa = ""

if (initial_count == 1):
    shutil.copy(path_setari_custom + "/setari_default.txt", path_setari_ram)
    nume_setare_aleasa = "setari_default.txt"
else:

    while (True):
        print("Alegeti setarea: ")

        nume_setare_aleasa = input() + ".txt"

        # with open(path_setari_custom + "/setari_default.txt", "r") as file:
        #  first_line = file.readline()
        #  for last_line in file:
        #      pass
        #   print(last_line)
        try:
            shutil.copy(path_setari_custom + "/" + nume_setare_aleasa, path_setari_ram)
            break
        except:
            print("Setarea aceasta nu exista! Incercati din nou")

# Redenumire
path_ram_abs = path_setari_utilizatori_abs + "/RAM/"
os.rename(path_ram_abs + nume_setare_aleasa, path_ram_abs + "fisier_ram.txt")
