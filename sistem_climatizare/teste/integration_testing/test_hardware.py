import __init__
import pytest
import threading
import time
from sistem_climatizare.hardware import Hardware
from sistem_climatizare.display import Display

test_passed = None


def test_hardware_loop():
    hardware = Hardware()
    t = threading.Thread(target=hardware.hardware_loop)
    t.start()
    time.sleep(5)
    hardware.stop()
    t.join()


def test_display_loop():
    display = Display()
    t = threading.Thread(target=display.display_loop)
    t.start()
    time.sleep(5)
    display.stop()
    t.join()
