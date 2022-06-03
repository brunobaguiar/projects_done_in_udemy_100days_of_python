from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

SEARCH_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSd80imLcpbpPWGtrc_h0U3Ae8p-1rHGlrjZ2yVlOwOsehsf0A/viewform?usp=sf_link"

driver = webdriver.Chrome()
driver.get(SEARCH_URL)
time.sleep(3)

actions = ActionChains(driver)
for _ in range(10):
    actions.send_keys(Keys.PAGE_DOWN)
    actions.perform()
    time.sleep(0.2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

link_list = []
address_list = []
price_list = []

card_link = driver.find_elements(By.CLASS_NAME, 'list-card-top')
card_address = driver.find_elements(By.CLASS_NAME, "list-card-addr")
card_price = driver.find_elements(By.CLASS_NAME, "list-card-price")

for card in card_link:
    link = card.find_element(By.CSS_SELECTOR, "a")
    link_list.append(link.get_attribute("href"))
for address in card_address:
    address_list.append(address.text)
for price in card_price:
    price_list.append(price.text.replace("/mo",""))

print(link_list)
print(len(link_list))
print(address_list)
print(len(address_list))
print(price_list)
print(len(price_list))


for n in range(len(address_list)-1):
    driver.get(FORM_URL)
    time.sleep(2)
    link_box = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_box.send_keys(link_list[n])
    address_box = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_box.send_keys(address_list[n])
    price_box = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_box.send_keys(price_list[n])
    send_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    send_button.click()
    time.sleep(3)

driver.quit()