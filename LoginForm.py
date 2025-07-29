from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.get('https://practicetestautomation.com/practice-test-login/')

driver.maximize_window()

WebDriverWait(driver, 10)

homepageTitle = driver.title
print('Home Page Title:' +homepageTitle)

assert homepageTitle in driver.page_source

driver.find_element(By.ID,'username').send_keys('student')
driver.find_element(By.ID,'password').send_keys('Password123')

driver.find_element(By.ID,'submit').click()

WebDriverWait(driver, 10)

assert 'Logged In Successfully' in driver.page_source

driver.quit()