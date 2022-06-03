# Start Selenium (only works with chrome driver inside python folder)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions

opt = Options()
opt.headless = True

driver = webdriver.Chrome()

# Open a webpage
driver.get("https://www.python.org/")

event_times = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget time')
# print(event_times)
# for time in event_times:
    # print(time.text)

event_names = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget li a')
# print(event_names)
# for name in event_names:
#     print(name.text)

events={}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)


driver.quit()
