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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.CSS_SELECTOR,"div[class='products'] div[class='product']")
count = len(results)
print(results)
assert count>0
for result in results:
    result.find_element(By.CSS_SELECTOR, "button[type='button']").click()

#time.sleep(1)
# div[class='products'] div[class='product'] button[type='button']

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#Sum validation
prices = driver.find_elements(By.XPATH,"//td[5]/p[@class='amount']")
sum=0
for price in prices:
    sum = sum + int(price.text)

total = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == total


driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
#time.sleep(1)
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
#time.sleep(5)
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
if driver.find_element(By.CLASS_NAME,"promoInfo").text == "Code applied ..!":
    print("Code applied")

afterDiscount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert afterDiscount<total