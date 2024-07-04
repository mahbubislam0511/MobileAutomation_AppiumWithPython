import pytest


@pytest.fixture(scope="module")
def setup():
    print("setup module level")
    yield
    print("teardown module level")


@pytest.fixture(scope="function")
def before():
    print("setup function level")
    yield
    print("teardown module function")


def test_AddUser(setup, before):
    print("User is added")


@pytest.mark.usefixtures("setup", "before")
@pytest.mark.regression
def test_EditeUser(setup, before):
    print("User is edited")


@pytest.mark.usefixtures("setup", "before")
@pytest.mark.sanity
def test_DeleteUser(setup, before):
    print("User is deleted")

