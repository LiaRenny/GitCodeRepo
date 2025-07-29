from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://www.google.com/")
title = driver.title
print(title)