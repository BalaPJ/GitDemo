import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()

assert not driver.find_element(By.ID,"displayed-text").is_displayed()

