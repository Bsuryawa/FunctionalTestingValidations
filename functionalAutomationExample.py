import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service (r"C:\Users\BHAGYASHRI\Downloads\chromedriver_win32 (1)\chromedriver")
driver =webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window
driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
time.sleep(2)
vegitables = driver.find_elements(By.XPATH, "//div[@class='product']")
#print(len(vegitables))
count = len(vegitables)
assert count > 0
#chaining the webelement
expectedList = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg" ]
actualList =[]
for vegitable in vegitables:
    actualList.append(vegitable.find_element(By.XPATH, "h4").text)
    vegitable.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()
assert expectedList == actualList
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, " tr td:nth-child(5) p")
sum =0
for price in prices:
    sum = sum + int(price.text)
print(sum)
totalAmount = int(driver.find_element(By.CLASS_NAME, "totAmt").text)
assert sum == totalAmount
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

discountedAmount = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)
assert  totalAmount > discountedAmount

driver.close()