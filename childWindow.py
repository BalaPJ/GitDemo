from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT,"Click Here").click()

openedWindows = driver.window_handles
driver.switch_to.window(openedWindows[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()
driver.switch_to.window(openedWindows[0])
print(driver.find_element(By.TAG_NAME,"h3").text)