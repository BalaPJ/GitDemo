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
driver.get("https://rahulshettyacademy.com/angularpractice")

driver.find_element(By.CSS_SELECTOR,"a[href='/angularpractice/shop']").click()

products = driver.find_elements(By.CSS_SELECTOR,"div[class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH,"div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class*='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR,"div[class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
successText = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in successText