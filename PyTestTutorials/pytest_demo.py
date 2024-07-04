import pytest

from PyTestTutorials import readData


def setup_function(function):
    print("Running in function level")


def teardown_function(function):
    print("Closing Tear Down in function")


def setup_module(module):
    print("Running in module level")


def teardown_module(module):
    print("Closing Tear Down in module")


def test_demo():
    print("Demo Pytest", readData.readConfigData.getURL())


def test_demo2():
    print("Demo Pytest2")
