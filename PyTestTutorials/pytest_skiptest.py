import pytest


@pytest.mark.skip
def test_skip():
    print("Skip this function")


def test_add():
    print("Add User")
