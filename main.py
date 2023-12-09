import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Balaji PJ")
driver.find_element(By.NAME, "email").send_keys("balaji@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Pass@1234")
driver.find_element(By.CSS_SELECTOR, "input[id='exampleCheck1']").click()
# driver.find_element(By.ID, "exampleFormControlSelect1").is_selected("Female")
driver.find_element(By.XPATH, "//input[@id='inlineRadio2']").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Dummy description")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(1)
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
