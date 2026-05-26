import time
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser_name",action="store",default="chrome",help="browser selection")

@pytest.fixture(scope="function")
def test_browser_instance(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        options = Options()
        options.binary_location = "/usr/bin/google/chrome/"
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-dev-shm-usage")
        service = Service("/usr/bin/")
        driver = webdriver.Chrome(service=service,options=options)
        #driver = webdriver.Chrome()
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
