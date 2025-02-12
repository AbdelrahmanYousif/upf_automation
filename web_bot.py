from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.example.com/")

print(driver.title)

time.sleep(5)

driver.quit()