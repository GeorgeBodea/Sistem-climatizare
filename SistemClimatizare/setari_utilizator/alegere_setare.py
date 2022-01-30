import pathlib
import shutil
import os
from variables import path_setari_custom, path_setari_ram, path_setari_utilizatori_abs



initial_count = 0
for path in pathlib.Path(path_setari_custom).iterdir():
    if path.is_file():
        initial_count += 1

print(initial_count)


nume_setare_aleasa = ""

if (initial_count != 1):
  while (True):
    print("Alegeti setarea: ")

    nume_setare_aleasa = input() + ".txt"

    try:
      data = ""
      with open(path_setari_custom + "/" + nume_setare_aleasa, "r") as fisier_setare:
        data = fisier_setare.read()

      with open(path_setari_ram + '/fisier_ram.txt', "w") as myfile:
        myfile.write(data)
      
      break
    except: 
      print("Setarea aceasta nu exista! Incercati din nou")



