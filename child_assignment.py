import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CSS_SELECTOR,".blinkingText").click()

window = driver.window_handles
driver.switch_to.window(window[1])
email = driver.find_element(By.CSS_SELECTOR,"a[href='mailto:mentor@rahulshettyacademy.com']").text
print(email)
driver.switch_to.window(window[0])

driver.find_element(By.CSS_SELECTOR,"input[id='username']").send_keys(email)
driver.find_element(By.CSS_SELECTOR,"input[id='password']").send_keys("learning")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(2)
print(driver.find_element(By.CSS_SELECTOR,"div[class='alert alert-danger col-md-12']").text)