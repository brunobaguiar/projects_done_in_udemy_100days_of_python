# Start Selenium (only works with chrome driver inside python folder)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = Options()
opt.headless = True

driver = webdriver.Chrome()

# Open a webpage
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(by=By.NAME, value="fName")
lname = driver.find_element(by=By.NAME, value="lName")
email = driver.find_element(by=By.NAME, value="email")
button = driver.find_element(by=By.CSS_SELECTOR, value="form button")
fname.send_keys("Bruno")
lname.send_keys("Nabashi")
email.send_keys("your@email.com")
button.click()