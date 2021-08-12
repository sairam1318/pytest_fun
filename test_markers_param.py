
import pytest
import sys

@pytest.mark.parametrize("Username, password", 
                        [
                            ("sairam", "tecnics"),
                            ("Raam", "IBM"),
                            ("David", "Oracle")
                        ]
)
def test_login(Username, password):
    print(Username)
    print(password)