import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

load_dotenv()
LINKEDIN_USERNAME = os.getenv("LINKEDIN_USERNAME")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")

chrome_driver = "D:/Documents/2022 Python Bootcamp/selenium/chromedriver.exe"
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(3)

username_form = driver.find_element(By.ID, "username")
username_form.send_keys(LINKEDIN_USERNAME)
password_form = driver.find_element(By.ID, "password")
password_form.send_keys(LINKEDIN_PASSWORD)
password_form.send_keys(Keys.ENTER)

# find all job elements from left hand column
driver.maximize_window()
job_elements = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")

# create list from elements
all_jobs = [job.text for job in job_elements]
print(all_jobs)
# click individual job element then click apply now
x = range(len(all_jobs))
for n in x:
    try:
        job_elements[n].click()

        time.sleep(5)
        apply_now = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        apply_now.click()
        # check for Submit application button vs Next (stores button text as button_text)
        button = driver.find_element(By.CSS_SELECTOR, "form button span")
        button_text = button.text
        print(button_text)

        # if Next, close window and click discard button, then continue loop
        # if Submit application, click button, break loop
        if button_text == "Next":
            dismiss = driver.find_element(By.XPATH, '//*[@aria-label="Dismiss"]')
            dismiss.click()
            discard = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
            discard.click()
        else:
            submit = driver.find_element(By.XPATH, '//*[@aria-label="Submit application"]')
            submit.click()
            break
    except NoSuchElementException as e:
        print(f"Error: {e}")
        continue
