from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

import time

from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)


# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com")
search_bar = driver.find_element(By.ID,"APjFqb")
search_bar.send_keys("sudharshan paul ganta")

search_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
search_btn.click()

first_link = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a')
first_link.click()

time.sleep(100)
driver.close()