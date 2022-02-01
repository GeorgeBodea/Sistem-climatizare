import pathlib
from variables import path_setari_custom_abs, path_setari_ram_abs, nume_fisier_ram


def suprascriere_fisier_ram(nume_setare, data=None):
    nume_fisier_setare = nume_setare + ".json"

    if data is None:
        with open(path_setari_custom_abs + "/" + nume_fisier_setare, "r") as fisier_setare:
            data = fisier_setare.read()

    with open(path_setari_ram_abs + nume_fisier_ram, "w") as myfile:
        myfile.write(data)


def nr_fisiere():
    count = 0
    for path in pathlib.Path(path_setari_custom_abs).iterdir():
        if path.is_file():
            count += 1
    return count


if __name__ == "__main__":
    while True:
        try:
            initial_count = nr_fisiere()
            print("Exista {} fisiere".format(initial_count))
            if initial_count == 1:
                suprascriere_fisier_ram("setari_default")
                print("Se utilizeaza setarile default")
            else:
                nume_setare_aleasa = input("Alegeti setarea: ")
                suprascriere_fisier_ram(nume_setare_aleasa)
        except Exception as e:
            print(e)
        else:
            print("Succes!")
            break
