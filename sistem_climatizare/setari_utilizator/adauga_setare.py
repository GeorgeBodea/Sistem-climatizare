import __init__
import json
from sistem_climatizare.setari_utilizator.variables import path_setari_custom_abs, get_data_curenta


def adaugare_setare_fct(nume_setare_custom, temperatura_dorita, numar_persoane):
    nume_fisier = path_setari_custom_abs + "/" + nume_setare_custom

    setari = dict()
    setari["Nume_Setare"] = nume_setare_custom
    setari["Numar_Persoane"] = numar_persoane
    setari["Temperatura"] = temperatura_dorita
    setari["Data_Creare"] = get_data_curenta()

    with open(nume_fisier + ".json", "w") as f:
        json.dump(setari, f, indent=2)
        f.write('\n')


if __name__ == "__main__":
    while True:
        try:
            nume_setare = input("Dati un nume setarii: ").strip()
            if nume_setare == "":
                raise Exception("Nume setare obligatoriu")
            temperatura = float(input("Dati o temperatura: "))
            nr_persoane = int(input("Dati numarul de persoane: "))

            adaugare_setare_fct(nume_setare, numar_persoane=nr_persoane, temperatura_dorita=temperatura)
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            print("Cancelled!")
            break
        else:
            print("Succes!")
            break
