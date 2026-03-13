from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

table_element = driver.find_element(By.ID,"product")
driver.execute_script("arguments[0].scrollIntoView(true);",table_element)
def getdata(rowindex,colindex):
    table_rows = driver.find_element(By.ID,"product").find_elements(By.TAG_NAME,"tr")
    table_definitions = table_rows[rowindex+1].find_elements(By.TAG_NAME,"td")
    return table_definitions[colindex].get_attribute("innerText")
print(getdata(0,1))

time.sleep(10)

