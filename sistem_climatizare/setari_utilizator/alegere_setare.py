import __init__
import pathlib
from sistem_climatizare.setari_utilizator.variables import path_setari_custom_abs, path_setari_ram_abs, nume_fisier_ram


def suprascriere_fisier_ram(nume_setare, data=None):
    nume_fisier_setare = nume_setare + ".json"

    if data is None:
        with open(path_setari_custom_abs + nume_fisier_setare, "r") as fisier_setare:
            data = fisier_setare.read()

    with open(path_setari_ram_abs + nume_fisier_ram, "w") as myfile:
        myfile.write(data)


def nr_fisiere(verbose=False):
    try:
        count = 0
        for path in pathlib.Path(path_setari_custom_abs).iterdir():
            if path.is_file():
                if verbose:
                    print(path)
                count += 1
        if verbose:
            print("Exista {} fisiere".format(count))
        return count
    except Exception as e:
        print(e)
        return 1


def alegere_setare_fct(nume_setare):
    nume_setare = nume_setare.strip()
    initial_count = nr_fisiere()
    if initial_count == 1:
        suprascriere_fisier_ram("setari_default")
        print("Se utilizeaza setarile default")
    else:
        suprascriere_fisier_ram(nume_setare)


if __name__ == "__main__":
    nr_fisiere(verbose=True)
    while True:
        try:
            nume_setare_aleasa = input("Alegeti setarea: ")
            alegere_setare_fct(nume_setare_aleasa)
        except Exception as e:
            print(e)
        else:
            print("Succes!")
            break
