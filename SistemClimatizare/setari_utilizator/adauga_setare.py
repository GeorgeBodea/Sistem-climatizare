import datetime
from variables import path_setari_custom_abs

nume_setare_custom = input("Dati un nume setarii: ")
temperatura_dorita = float(input("Dati o temperatura: "))
numar_persoane = int(input("Dati numarul de persoane: "))

current_time = datetime.datetime.now()
data_curenta = str(current_time).split('.')[0]

nume_fisier = path_setari_custom_abs + "/" + nume_setare_custom

f = open(nume_fisier + ".txt", "w+")
f.write(
    "Nume_Setare: " + nume_setare_custom + '\n' +
    "Numar_Persoane: " + str(numar_persoane) + '\n' +
    "Temperatura: " + str(temperatura_dorita) + '\n' +
    "Data_Creare: " + data_curenta
)
f.close()
