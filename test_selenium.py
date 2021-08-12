import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = None

@pytest.fixture
def setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.quit()

def test_chrome(setup):
    driver.get("http://www.fb.com")
    print("open chrome")

def test_apple(setup):
    driver.get("http://www.apple.com")
    print("open apple")