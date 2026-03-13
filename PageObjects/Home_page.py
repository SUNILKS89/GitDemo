from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Expected_Conditions

class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.homepage_button =(By.CSS_SELECTOR, "ul.tb-megamenu-nav > li.tb-megamenu-item:nth-child(1)")
        self.homepage_submenu=(By.CSS_SELECTOR,
                   "#tb-megamenu-column-1 > div.tb-megamenu-column-inner > ul.tb-megamenu-subnav > li.tb-megamenu-item:nth-child(1) > a")
    def goto_homepage(self):
        element = self.driver.find_element(*self.homepage_button )
        ActionChains(self.driver).move_to_element(element).perform()

    def goto_homepage_submenu(self):
        wait = WebDriverWait(self.driver, 10)
        submenu_list = wait.until(Expected_Conditions.visibility_of_element_located(self.homepage_submenu))
        submenu_list.click()