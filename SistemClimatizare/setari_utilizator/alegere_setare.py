import pathlib
from variables import path_setari_custom_abs, path_setari_ram_abs



initial_count = 0
for path in pathlib.Path(path_setari_custom_abs).iterdir():
    if path.is_file():
        initial_count += 1



def suprascriere_fisier_ram(nume_setare):
  nume_fisier_setare = nume_setare + ".txt"
  data = ""
  
  with open(path_setari_custom_abs + "/" + nume_fisier_setare, "r") as fisier_setare:
    data = fisier_setare.read()

  with open(path_setari_ram_abs + '/fisier_ram.txt', "w") as myfile:
    myfile.write(data)




if (initial_count == 1):
  suprascriere_fisier_ram("setari_default")
else:
  while (True):
    nume_setare_aleasa = input("Alegeti setarea: ")

    try:
      suprascriere_fisier_ram(nume_setare_aleasa)
      break
    except: 
      print("Setarea aceasta nu exista! Incercati din nou")



