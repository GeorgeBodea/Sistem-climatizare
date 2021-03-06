import __init__
import pytest
import sistem_climatizare.setari_utilizator.adauga_setare as adauga_setare
import sistem_climatizare.setari_utilizator.alegere_setare as alegere_setare
import sistem_climatizare.setari_utilizator.stergere_setare as stergere_setare
import sistem_climatizare.setari_utilizator.variables as variables
from sistem_climatizare.setari_utilizator.variables import path_setari_custom_abs, path_setari_ram_abs, nume_fisier_ram
import json
import os


def my_test_adaugare_setare_fct(nume_setare, temperatura, numar_persoane):
    # exemplu apelare functie: pytest -s teste_setari.py --nume_setare setare1
    nume_fisier = path_setari_custom_abs + nume_setare + '.json'
    json_before = None

    if os.path.isfile(nume_fisier):
        # caut sa vad daca exista deja un json pentru aceasta setare
        with open(nume_fisier) as f:
            json_before = json.load(f)

    # apelez functia de adaugare pe care doresc sa o testez
    try:
        adauga_setare.adaugare_setare_fct(nume_setare, temperatura, numar_persoane)
    except ValueError:
        assert nume_setare == "Default"
    else:
        if json_before is None:
            # daca setarea a fost noua, verific sa vad c s-a creat jsonul corespunzator
            assert os.path.isfile(nume_fisier)
        else:
            # daca setarea exista deja de la inceput
            with open(nume_fisier) as f:
                # preiau jsonul actual al setarii
                json_after = json.load(f)

            # si verific ca acesta sa fi fost updatat (trebuie sa fie updatata cel putin ora)
            assert json_before != json_after


def test_adaugare_setare_default():
    my_test_adaugare_setare_fct('Default', 1, 10)


def test_adaugare_setare_noua():
    my_test_adaugare_setare_fct('Qwerty.test', 12, 13)


def test_adaugare_setare_existenta():
    my_test_adaugare_setare_fct('Qwerty.test', 10, 10)
    my_test_adaugare_setare_fct('Qwerty.test', 13, 14)


def setarea_nu_exista(setare):
    setari = variables.lista_nume_setari

    for json_name in setari:
        print(json_name + ' si ' + json_name[:-5])
        if json_name[:-5] == setare:
            return False

    return True


def my_test_alegere_setare(setare_aleasa):
    # exemplu apelare: pytest -s teste_setari.py --setare_aleasa setare_inexistenta
    # daca arunca exceptia, inseamna ca setarea aleasa nu exista (verific asta)
    # altfel, testarea pe care am ales-o exista, verific ca s-a suprascris corect fisierul ram
    try:
        alegere_setare.alegere_setare_fct(setare_aleasa)
        with open(path_setari_custom_abs + "/" + setare_aleasa + '.json', "r") as fisier_setare:
            data = fisier_setare.read()

    except FileNotFoundError:
        assert setarea_nu_exista(setare_aleasa)

    else:
        with open(path_setari_ram_abs + nume_fisier_ram, "r") as fisier_ram:
            data2 = fisier_ram.read()

        assert data == data2


def test_alegere_setare_dault():
    my_test_alegere_setare('Default')


def test_alegere_setare_inexistent():
    my_test_alegere_setare('Inexistent...')


def my_test_stergere_setare_fct(setare_de_sters):
    # exemplu apelare: pytest -s teste_setari.py --setare_aleasa setare_inexistenta
    nu_exista = None
    try:
        nu_exista = setarea_nu_exista(setare_de_sters)
        stergere_setare.stergere_setare_fct(setare_de_sters)

    except FileNotFoundError:
        assert nu_exista

    except ValueError:
        assert setare_de_sters == "Default"

    else:
        assert setarea_nu_exista(setare_de_sters)


def test_stergere_setare_default():
    my_test_stergere_setare_fct('Default')


def test_stergere_setare_corecta():
    my_test_stergere_setare_fct('Qwerty.test')


def test_stergere_setare_inexistenta():
    my_test_stergere_setare_fct('Inexistent...')


def test_nr_fisiere_alegere_setare():
    assert len(variables.get_lista_nume_setari()) == alegere_setare.nr_fisiere()


def test_suprascriere_fisier_ram():
    alegere_setare.suprascriere_fisier_ram('Default')
    with open(path_setari_custom_abs + 'Default.json', 'r') as f1:
        with open(path_setari_ram_abs + nume_fisier_ram, 'r') as f2:
            assert f1.read() == f2.read()
