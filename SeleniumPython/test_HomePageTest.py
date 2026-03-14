import json
import time
import sys
import os
import pytest
# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PageObjects.Home_page import HomePage


test_data_path = "Data/test_e2eTestFramework.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_data_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.order(2)
def test_random():
    print("random test")
    print("branch: develop2")
    # homepage.goto_homepage()#failed test case for testing running only failed tests using "pytest --lf"

#@pytest.mark.parametrize("test_list_item",test_data_list)
@pytest.mark.order(1)
# @pytest.mark.dependency(depends=['test_random'])
def test_home_page(test_browser_instance):
    driver = test_browser_instance
    driver.get("https://www.pragati-automation.com/")

    print(driver.title)
    homepage = HomePage(driver)
    homepage.goto_homepage()
    homepage.goto_homepage_submenu()
    #driver.back()
    time.sleep(5)

