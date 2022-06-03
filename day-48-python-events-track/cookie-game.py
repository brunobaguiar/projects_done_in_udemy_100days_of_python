from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

opt = Options()
opt.headless = True

driver = webdriver.Chrome()

# Open a webpage
driver.get("http://orteil.dashnet.org/experiments/cookie/")

#Get cookie to click on.
cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 2
five_min = time.time() + 60*5 # 5minutes

while True:
    cookie.click()

    # # Every 5 seconds:
    if time.time() > timeout:
        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))

        prices_list = []

        buyGrandma = driver.find_element(By.ID, "buyGrandma")
        Grandma = int(buyGrandma.text.split()[2].replace(",", "")) / 1
        prices_list.append(Grandma)
        buyFactory = driver.find_element(By.ID, "buyFactory")
        Factory = int(buyFactory.text.split()[2].replace(",", "")) / 4
        prices_list.append(Factory)
        buyMine = driver.find_element(By.ID, "buyMine")
        Mine = int(buyMine.text.split()[2].replace(",", "")) / 10
        prices_list.append(Mine)
        buyShipment = driver.find_element(By.ID, "buyShipment")
        Shipment = int(buyShipment.text.split()[2].replace(",", "")) / 20
        prices_list.append(Shipment)

        buy_index = prices_list.index(min(prices_list))

        if buy_index == 0 and money > prices_list[0]:
            buyGrandma.click()
        elif buy_index == 1 and money > prices_list[1]:
            buyFactory.click()
        elif buy_index == 2 and money > prices_list[2]:
            buyMine.click()
        elif buy_index == 3 and money > prices_list[3]:
            buyShipment.click()

        timeout = time.time() + 2

    # After 5 minutes:
    if time.time() > five_min:
        cookie_per_second = driver.find_element(By.ID, "cps")
        print(cookie_per_second.text)
        break
