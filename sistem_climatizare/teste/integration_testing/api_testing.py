import __init__
from input_output_helper import get_display_output, set_keyboard_input
import pytest
import pathlib
import runpy
import sistem_climatizare.api_http.app as app
from sistem_climatizare.setari_utilizator.variables import path_setari_custom_abs, get_data_curenta, path_setari_ram_abs, nume_fisier_ram
import json
import os


@pytest.fixture(autouse=True)
def run_around_tests():
    # Code that will run before your test, for example:
    files_before = # ... do something to check the existing files
    # A test function will be run at this point
    yield
    # Code that will run after your test, for example:
    files_after = # ... do something to check the existing files
    assert files_before == files_after


# def test_
