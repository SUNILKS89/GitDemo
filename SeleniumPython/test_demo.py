import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

def test_demo():
    driver = webdriver.Chrome()
    file_path ="/home/sunil-k-s/Downloads/download.xlsx"
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
    time.sleep(5)
    #sending CONTROL+SHIFT+S keys at a time
    #ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('s').key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()
    element = driver.find_element(By.CSS_SELECTOR,"input[type='file']")
    element.send_keys(file_path)

    time.sleep(5)
    driver.implicitly_wait(5)