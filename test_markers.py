import pytest


@pytest.mark.smoke
def test_login():
    print("Login")

@pytest.mark.regression
def test_logout():
    print("Logout")