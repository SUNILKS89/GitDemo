import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Expected_Conditions

#selenium grid to run scripts on remote machine
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#REMOTE_URL = "http://client-server-ip:4444/wd/hub"
#capabilities = DesiredCapabilities.CHROME.copy()
#capabilities['browserName']="chrome"
#capabilities['platform']='linux'
#capabilities['acceptInsecureCerts'] = True
#webdriver.Remote(command_executor=REMOTE_URL,desired_capabilities=capabilities)
# Run test on remote machine
# driver.get("https://example.com")
# print(driver.title)


driver = webdriver.Chrome()
file_path ="/home/sunil-k-s/Downloads/download.xlsx"
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

wait =WebDriverWait(driver,10)


textbox = driver.find_element(By.ID, "autocomplete")

driver.execute_script("arguments[0].setAttribute('disabled','true');", textbox)
time.sleep(5)
driver.execute_script("arguments[0].removeAttribute('disabled');",textbox)
textbox.send_keys("Hello World")

#alert
driver.find_element(By.ID,"alertbtn").click()
#if 'alert_is_present()' is used with explicit wait, it will wait for set time & switch to alert window, no need to
#use 'driver.switch_to.alert'
alert_window = wait.until(Expected_Conditions.alert_is_present())
#alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.accept()

#scrolling
element = driver.find_element(By.CSS_SELECTOR,"div.block.large-row-spacer > fieldset > legend")

#Can you explain how you can handle colors in a web driver
color = element.value_of_css_property('color')
print(Color.from_string(color).hex)
print(color)

#ActionChains(driver).move_to_element(element).perform() #using ActionChains()
driver.execute_script("arguments[0].scrollIntoView({block:'center'});",element)

wait.until(Expected_Conditions.visibility_of_element_located((By.CSS_SELECTOR,"div.block.large-row-spacer > fieldset > legend")))
#iframe testing
#driver.switch_to.frame(driver.find_element(By.ID,"courses-iframe"))#switching to iframe using ID
driver.switch_to.frame(0)#switching to iframe using index
driver.find_element(By.CSS_SELECTOR,"div.top-right.clearfix > div:nth-child(2).login-btn").click()


time.sleep(5)
driver.implicitly_wait(5)