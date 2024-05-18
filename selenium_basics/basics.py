import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from shutil import which

option = Options()
option.add_argument("--headless")

chrome_path = which("chromedriver")

service = Service(executable_path=chrome_path)
# option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)
driver.get("https://duckduckgo.com")
# time.sleep(45)

# search_input = driver.find_element(By.XPATH, '//input[contains(@id, "searchbox_input")]')
search_input = driver.find_element(By.ID, "searchbox_input")
search_input.send_keys("My User Agent")
# search_btn = driver.find_element(By.CLASS_NAME, "searchbox_iconWrapper__suWUe")
# search_btn.click()

search_input.send_keys(Keys.ENTER)
# time.sleep(40)

print(driver.page_source)
driver.close()

