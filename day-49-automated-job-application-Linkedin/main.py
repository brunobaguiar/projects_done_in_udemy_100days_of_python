from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?keywords=python%20developer"

opt = Options()
opt.headless = True

driver = webdriver.Chrome()

# Open a webpage
driver.get(LINKEDIN_URL)

enter_login = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
enter_login.click()

time.sleep(1)

user_field = driver.find_element(By.NAME, "session_key")
user_field.send_keys("your@gmail.com")
password_field = driver.find_element(By.NAME, "session_password")
password_field.send_keys("abcdef123456")

enter_login2 = driver.find_element(By.CLASS_NAME, "btn__primary--large")
enter_login2.click()

time.sleep(1)

list_jobs = driver.find_elements(By.CLASS_NAME, "job-card-container__metadata-item--workplace-type")

time.sleep(1)

for job in list_jobs:
    job.click()
    time.sleep(1)
    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_button.click()
    save_button.send_keys(Keys.END)

    time.sleep(1)
    follow_button = driver.find_element(By.CLASS_NAME, "follow")
    follow_button.click()
