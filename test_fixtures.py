import pytest

@pytest.fixture
def setup():
    print("Start")
    yield
    print("Stop")


def test_login(setup):
    print("login")


def test_checkin(setup):
    print("checkin")

def test_logout():
    print("logout")