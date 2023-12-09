import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_element(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(countries)

for country in countries:
    if country.text == "India":
        country.click()
        break

