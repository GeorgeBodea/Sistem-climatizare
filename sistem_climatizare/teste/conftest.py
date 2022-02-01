import pytest


# @pytest.fixture
def pytest_addoption(parser):
    parser.addoption("--nume_setare", action="store", default="default name")
    parser.addoption("--temperatura", action="store", default="0")
    parser.addoption("--numar_persoane", action="store", default="0")
    parser.addoption("--setare_aleasa", action="store", default="setare1")


def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value1 = metafunc.config.option.nume_setare
    option_value2 = metafunc.config.option.temperatura
    option_value3 = metafunc.config.option.numar_persoane
    option_value4 = metafunc.config.option.setare_aleasa

    if 'nume_setare' in metafunc.fixturenames and option_value1 is not None:
        metafunc.parametrize("nume_setare", [option_value1])

    if 'nume_setare' in metafunc.fixturenames and option_value2 is not None:
        metafunc.parametrize("temperatura", [option_value2])

    if 'nume_setare' in metafunc.fixturenames and option_value3 is not None:
        metafunc.parametrize("numar_persoane", [option_value3])

    if 'setare_aleasa' in metafunc.fixturenames and option_value4 is not None:
        metafunc.parametrize("setare_aleasa", [option_value4])
