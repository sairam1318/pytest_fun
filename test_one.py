
def test_method():
    x = 5
    assert x > 4

# this will not run

def method2():
    x = 10
    y = 20
    assert x < y

# this will not run

def method_test():
    name = "JayaSairam"
    main = "Sairam"
    assert name in main

def test_love():
    name = "JayaSairam"
    main = "Sairam"
    assert main in name

def test_other():
    name="Sairam"
    fullName = "JayaSairam"
    assert name in fullName, "Will get printed instead of assertion error if test fails"

