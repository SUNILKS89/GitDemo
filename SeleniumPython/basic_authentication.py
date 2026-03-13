import base64

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

#This method uses Chrome DevTools Protocol (CDP) to handle Basic HTTP Authentication pop-ups in modern Chrome.
driver.execute_cdp_cmd("Network.enable",{})
credentials = "admin:admin"
encoded_credentials = base64.b64encode(credentials.encode()).decode()
driver.execute_cdp_cmd("Network.setExtraHTTPHeaders",{"headers":{"Authorization":f"Basic {encoded_credentials}"}})


driver.get("https://the-internet.herokuapp.com/basic_auth")

print(driver.current_url)


time.sleep(5)
