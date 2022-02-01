import json
import sys

sys.path.append("../firebase_backup")
import firebase_api

from variables import path_setari_custom_abs, get_data_curenta


def adaugare_setare_fct(nume_setare_custom, temperatura_dorita, numar_persoane, email, password):
    nume_fisier = path_setari_custom_abs + "/" + nume_setare_custom

    setari = dict()
    setari["Nume_Setare"] = nume_setare_custom
    setari["Numar_Persoane"] = numar_persoane
    setari["Temperatura"] = temperatura_dorita
    setari["Data_Creare"] = get_data_curenta()
    setari["Email"] = email

    try:
        # daca se schimba emailul, va trebui sa stergem explicit inregistrarea din fosta baza de date
        with open(nume_fisier + ".json", "r") as f:
            setari_vechi = json.loads(f.read())
            if setari_vechi["Email"] != setari["Email"]:
                raise Exception("Nu aveti voie sa actualizati adresa de email!")
    except FileNotFoundError:
        pass  # daca nu exista fisierul, trecem direct la adaugare

    firebase_api.upload_setting(email, password, setari)

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
            new_email = input("Email: ").strip()
            new_password = input("Password: ").strip()
            if new_email == "" and new_password == "":
                new_email, new_password = firebase_api.test_email_password
            adaugare_setare_fct(nume_setare, numar_persoane=nr_persoane, temperatura_dorita=temperatura, email=new_email, password=new_password)
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            print("Cancelled!")
            break
        else:
            print("Succes!")
            break
