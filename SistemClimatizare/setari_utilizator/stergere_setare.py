import os
from variables import path_setari_custom_abs

if __name__ == "__main__":
    while True:
        nume_setare_custom = input("Stergeti setarea cu numele: ")

        path_setare = path_setari_custom_abs + "/" + nume_setare_custom
        nume_fisier_setare = path_setare + ".json"

        print('\n' + nume_fisier_setare)
        if os.path.exists(nume_fisier_setare):
            if (nume_setare_custom == "setari_default"):
                print("Setarea default nu se sterge")
                break
            os.remove(nume_fisier_setare)
            break
        else:
            print("Setarea nu exista")
