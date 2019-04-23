from nose.tools import *
from EX47.game import Room


def setup():
    print("Setup!")


def tear_down():
    print("Tear down")


def test_room():
    gold = Room("GoldRoom", 
            """This room has gold in it you can grab. There's a door to the north""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

