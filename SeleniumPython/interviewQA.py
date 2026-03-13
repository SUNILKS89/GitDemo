from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")


#drag and drop
driver.find_element(By.LINK_TEXT,"Drag and Drop").click()
source = driver.find_element(By.ID,"column-a")
target = driver.find_element(By.ID,"column-b")
ActionChains(driver).drag_and_drop(source,target).perform()


#screenshot
driver.get_screenshot_as_file("screenshot.png")

driver.back()
#drodown
driver.find_element(By.LINK_TEXT,"Dropdown").click()
dropdown = driver.find_element(By.ID,"dropdown")
select = Select(dropdown)
#select.select_by_index(2)

#use value from HTML tag <option value="1" selected="selected">Option 1</option>
#select.select_by_value("")

#select by text
select.select_by_visible_text("Option 2")

#mouse hovering
driver.back()
driver.find_element(By.LINK_TEXT,"Hovers").click()
element = driver.find_element(By.CSS_SELECTOR,"div.example > div.figure:nth-child(3) > img")
ActionChains(driver).move_to_element(element).perform()


time.sleep(10)