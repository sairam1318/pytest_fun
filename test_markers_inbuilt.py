import pytest
import sys

@pytest.mark.skip
def test_skip():
    print("This method will be skipped")

@pytest.mark.skipif(sys.version_info < (4, 0), reason="Python version is not supported")
def test_unskip():
    print("This method will be tested ")

@pytest.mark.xfail
def test_xfail():
    assert True
    print("logout")