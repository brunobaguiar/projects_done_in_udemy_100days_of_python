from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 100
PROMISED_UP = 50
TWITTER_URL = "https://twitter.com/"
TWITTER_EMAIL = "your@email.com"
TWITTER_PASSWORD = "your_password"
SPEED_TEST = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = ""
        self.up = ""
        self.driver = webdriver.Chrome()


    def get_internet_speed(self):
        self.driver.get(SPEED_TEST)
        start = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        start.click()
        time.sleep(45)
        results = self.driver.find_elements(By.CLASS_NAME, "result-data-value")
        self.down = float(results[1].text)
        self.up = float(results[2].text)
        return [self.down, self.up]

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        time.sleep(3)
        entrar = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')
        entrar.click()
        time.sleep(2)
        email = self.driver.find_element(By.CLASS_NAME, "r-fdjqy7")
        email.send_keys(TWITTER_EMAIL)
        time.sleep(2)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span')
        next_button.click()
        time.sleep(2)
        password = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        entrar2 = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/span/span')
        entrar2.click()

bot = InternetSpeedTwitterBot()
actual_speed = bot.get_internet_speed()

if actual_speed[0] < 250 or actual_speed[1]<150:
    bot.tweet_at_provider()
