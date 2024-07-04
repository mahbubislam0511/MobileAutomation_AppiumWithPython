import pytest


def getData():
    return [
        ('lokesh', '12345'),
        ('loki', '12345')
    ]


@pytest.mark.parametrize("userName, password", getData())
def test_login(userName, password):
    print("userName====", userName, "------", "password====", password)
