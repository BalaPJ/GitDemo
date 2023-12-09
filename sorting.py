import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

browserSortedList = []

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

browserSorted_webElements = driver.find_elements(By.XPATH, "//tr/td[1]")

for ele in browserSorted_webElements:
    browserSortedList.append(ele.text)

print(browserSortedList)

originalSortedList = browserSortedList.copy()

assert originalSortedList == browserSortedList

