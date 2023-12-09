import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("balaji@gmail.com")
driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("Pass@1234")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(3) input").send_keys("Pass@1234")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)