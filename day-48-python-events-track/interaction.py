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
driver.get("https://en.wikipedia.org/wiki/Main_Page")

number_en_articles = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="articlecount"]/a[1]')))

print(number_en_articles.text)

number_articles = driver.find_element(by=By.CSS_SELECTOR, value='#articlecount a')
print(number_articles.text)

# history = driver.find_element_by_link_text("View history")
history = driver.find_element(by=By.LINK_TEXT, value="View history")
# history.click()

# search = driver.find_element_by_name("search")
search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()