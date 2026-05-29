from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self,driver):
        self.driver = driver
        #self.homepage_button =(By.CSS_SELECTOR, "ul.tb-megamenu-nav > li.tb-megamenu-item:nth-child(1)")
        self.homepage_button = (By.XPATH,"//li[contains(@class,'tb-megamenu-item')]/a[normalize-space()='Home']")
        #self.homepage_submenu=(By.CSS_SELECTOR,"#tb-megamenu-column-1 > div.tb-megamenu-column-inner > ul.tb-megamenu-subnav > li.tb-megamenu-item:nth-child(1) > a")
        self.homepage_submenu=(By.XPATH,"//a[@href='/en/history' and normalize-space()='History']")
    def goto_homepage(self):
        wait = WebDriverWait(self.driver, 30)
        #wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        #element = self.driver.find_element(*self.homepage_button )
        element = wait.until(EC.visibility_of_element_located(self.homepage_button))
        self.driver.save_screenshot("jenkins_debug.png")
        #self.driver.execute_script("""var evt = new MouseEvent('mouseover', {bubbles: true,cancelable: true,view: window});arguments[0].dispatchEvent(evt);""", element)
        # scroll into view
        #self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        ActionChains(self.driver).move_to_element(element).pause(1).perform()
        

        #adding submenu() code here for testing
        submenu_list = wait.until(EC.element_to_be_clickable(self.homepage_submenu))
        submenu_list.click()

    def goto_homepage_submenu(self):
        wait = WebDriverWait(self.driver, 10)
        submenu_list = wait.until(Expected_Conditions.visibility_of_element_located(self.homepage_submenu))
        submenu_list.click()
