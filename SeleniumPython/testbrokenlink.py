from urllib.parse import urljoin, urlparse
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

broken_link= []
URL = "https://rahulshettyacademy.com/AutomationPractice/"
driver = webdriver.Chrome()
driver.get(URL)

def is_url_valid(url):
    parsed = urlparse(url)
    return bool(parsed.scheme) and bool(parsed.netloc)

links = driver.find_elements(By.TAG_NAME,"a")
print(f"Total links found:{len(links)}")

for link in links:
    href = link.get_attribute("href")
    if not href:
        continue

    href_abs = urljoin(URL,href)

    if not is_url_valid(href_abs):
        continue
    try:
        response = requests.head(href_abs,allow_redirects=True,timeout=10)
        if response.status_code >=400:
            print(f"Broken:{href} ({response.status_code})")
            broken_link.append(href)
        else:
            print(f"OK:{href}")

    except requests.exceptions.RequestException:
        print(f"Broken:{href} (Request failed)")
        broken_link.append(href)
print(f"Broken links found:{len(broken_link)}")


