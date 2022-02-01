import json

from variables import path_setari_custom_abs, get_data_curenta

def adaugare_setare_fct(nume_setare_custom, numar_persoane, temperatura_dorita):
        #nume_setare_custom = input("Dati un nume setarii: ").strip()
        #temperatura_dorita = float(input("Dati o temperatura: "))
        #numar_persoane = int(input("Dati numarul de persoane: "))

        nume_setare_custom = nume_setare_custom.strip()
        temperatura_dorita = float(temperatura_dorita)
        numar_persoane = int(numar_persoane)

        nume_fisier = path_setari_custom_abs + "/" + nume_setare_custom

        f = open(nume_fisier + ".json", "w")
        setari = dict()
        setari["Nume_Setare"] = nume_setare_custom
        setari["Numar_Persoane"] = numar_persoane
        setari["Temperatura"] = temperatura_dorita
        setari["Data_Creare"] = get_data_curenta()
        json.dump(setari, f, indent=2)
        f.write('\n')
        f.close()
