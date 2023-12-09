import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Balaji")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert "Balaji" in alertText
print(alertText)
alert.accept()