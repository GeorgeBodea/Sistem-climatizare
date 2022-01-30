import pathlib
from variables import path_setari_custom_abs, path_setari_ram_abs, nume_fisier_ram


def suprascriere_fisier_ram(nume_setare, data=None):
    nume_fisier_setare = nume_setare + ".json"

    if data is None:
        with open(path_setari_custom_abs + "/" + nume_fisier_setare, "r") as fisier_setare:
            data = fisier_setare.read()

    with open(path_setari_ram_abs + nume_fisier_ram, "w") as myfile:
        myfile.write(data)


if __name__ == "__main__":
    initial_count = 0
    for path in pathlib.Path(path_setari_custom_abs).iterdir():
        if path.is_file():
            initial_count += 1
    if initial_count == 1:
        suprascriere_fisier_ram("setari_default")
    else:
        while True:
            nume_setare_aleasa = input("Alegeti setarea: ")

            try:
                suprascriere_fisier_ram(nume_setare_aleasa)
                break
            except:
                print("Setarea aceasta nu exista! Incercati din nou")
