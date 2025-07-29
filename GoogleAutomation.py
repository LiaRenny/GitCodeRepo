from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.get("https://www.google.com/")

driver.maximize_window()

title = driver.title
print('Page Title: ' +title)

WebDriverWait(driver, 30)

driver.find_element(By.NAME,'q').send_keys('Automation with Selenium')

modal_close = driver.find_element(By.NAME,'btnK')

if modal_close.is_displayed():
    modal_close.click()
    print("Found")


WebDriverWait(driver, 200)

driver.quit()