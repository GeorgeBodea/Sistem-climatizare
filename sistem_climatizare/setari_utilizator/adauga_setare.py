import json
import sistem_climatizare.firebase_backup.firebase_api as firebase_api
from variables import path_setari_custom_abs, get_data_curenta

if __name__ == "__main__":
    while True:
        try:
            nume_setare_custom = input("Dati un nume setarii: ").strip()
            if nume_setare_custom == "":
                raise Exception("Nume setare obligatoriu")
            temperatura_dorita = float(input("Dati o temperatura: "))
            numar_persoane = int(input("Dati numarul de persoane: "))
            email = input("Email: ").strip()
            password = input("Password: ").strip()
            if email == "" or password == "":
                email, password = firebase_api.test_email_password
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
                        old_password = input("Password for {}: ".format(setari_vechi["Email"]))
                        firebase_api.delete_setting_by_key(setari_vechi["Email"], old_password, setari_vechi["Nume_Setare"])
            except FileNotFoundError:
                pass  # daca nu exista fisierul, trecem direct la adaugare

            with open(nume_fisier + ".json", "w") as f:
                json.dump(setari, f, indent=2)
                f.write('\n')

            firebase_api.backup_setting(email, password, setari)
        except Exception as e:
            print(e)
        else:
            print("Succes!")
            break
