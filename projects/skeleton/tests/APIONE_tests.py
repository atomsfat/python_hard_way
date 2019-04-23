from nose.tools import *
import APIONE


def setup():
    print("Setup!")


def tear_down():
    print("Tear down")


def test_basic():
    APIONE.emoji_screen()
