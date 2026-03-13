import time
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains, Keys


def pytest_addoption(parser):
    parser.addoption("--browser_name",action="store",default="chrome",help="browser selection")

@pytest.fixture(scope="function")
def test_browser_instance(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == 'edge':
        driver = webdriver.Edge()
    elif browser_name == "safari":
        driver = webdriver.Safari()
    elif browser_name == "Firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    #ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('s').key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()
    driver.implicitly_wait(5)
    yield driver
    driver.close()