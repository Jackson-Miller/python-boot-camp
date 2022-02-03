from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver = "D:/Documents/2022 Python Bootcamp/selenium/chromedriver.exe"
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(article_count.text)

driver.quit()
