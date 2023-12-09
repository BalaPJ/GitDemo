import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://kwschennai.com/#radar")

i=1

while i<2:
    driver.find_element(By.CSS_SELECTOR,"#alert alert--realtime alert--realtime--refresh alert--realtime--refresh-v2").click()
