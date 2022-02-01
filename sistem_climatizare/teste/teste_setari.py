from ast import Break
from logging import exception
from input_output_helper import get_display_output, set_keyboard_input
import pytest
import pathlib
import runpy

import sistem_climatizare.setari_utilizator.alegere_setare
from sistem_climatizare.setari_utilizator.variables import path_setari_custom_abs, get_data_curenta, path_setari_ram_abs, nume_fisier_ram
import json
import os


# def test_aux():
#     assert 5 == 3

# def test_citeste_setare():

#     citeste_setarea()
#     print ("Displaying name: %s" % nume_setare % temperatura % nr_persoane)


# def test_adauga_setare(nume_setare, temperatura, numar_persoane):
#     # exemplu apelare functie: pytest -s teste_setari.py --nume_setare setare1
#     nume_fisier = path_setari_custom_abs + nume_setare + '.json'
#     json_before = None

#     if os.path.isfile (nume_fisier):
#         with open(nume_fisier) as f:
#             json_before = json.load(f)

#     adauga_setare.adauga_setare(nume_setare, temperatura, numar_persoane)

#     with open(nume_fisier) as f:
#         json_after = json.load(f)

#     if json_before:
#         assert json_before != json_after
#     else:
#         assert  os.path.isfile (nume_fisier)


def setarea_nu_exista(setare):
    setari = os.listdir('../setari_utilizator/setari_custom')

    for json_name in setari:
        print(json_name + ' si ' + json_name[:-5])
        if json_name[:-5] == setare:
            return False

    return True


def test_alegere_setare(setare_aleasa):
    # exemplu apelare: pytest -s teste_setari.py --setare_aleasa setare_inexistenta

    # daca setarea aleasa nu exista, testez apoi pentru "default name" ca sa se opreasca while ul din alegere_setare.py
    # deoarece el ruleaza pana cand primeste o setare care exista.
    set_keyboard_input([setare_aleasa, 'setare_noua'])

    alegere_setare.alege_setare()

    out = get_display_output()

    if "Setarea aceasta nu exista! Incercati din nou" in out:
        # daca pentru setarea pe care am introdus-o am primit mesajul ca nu exista, verificam daca chiar n-a existat
        assert setarea_nu_exista(setare_aleasa)
    else:
        # daca testarea pe care am ales-o exista, verific ca s-a suprascris corect fisierul ram
        with open(path_setari_custom_abs + setare_aleasa + '.json', "r") as fisier_setare:
            data1 = fisier_setare.read()

        with open(path_setari_ram_abs + nume_fisier_ram, "r") as fisier_ram:
            data2 = fisier_ram.read()

        assert data1 == data2

# def pytest_exception_interact(node, call, report):
#     excinfo = call.excinfo
#     if 'script' in node.funcargs:
#         excinfo.traceback = excinfo.traceback.cut(path=node.funcargs['script'])
#     report.longrepr = node.repr_failure(excinfo)


# @pytest.mark.parametrize('script', scripts)
# def test_script_execution(script):
#     runpy.run_path(script)
