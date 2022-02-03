from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

chrome_driver = "D:/Documents/2022 Python Bootcamp/selenium/chromedriver.exe"
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)
driver.get("https://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Python")
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Python")
email = driver.find_element(By.NAME, "email")
email.send_keys("test@test.test")
email.send_keys(Keys.ENTER)

# driver.quit()
