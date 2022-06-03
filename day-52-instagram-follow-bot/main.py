from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

INSTAGRAM_URL = "https://www.instagram.com/accounts/login/"
USERNAME = "your_username"
PASSWORD = "your_password"
SIMILAR_ACCOUNT = "ocarteironft"

class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(INSTAGRAM_URL)
        self.login()

    def login(self):
        time.sleep(1)
        username_box = self.driver.find_element(By.NAME, "username")
        username_box.send_keys(USERNAME)
        password_box = self.driver.find_element(By.NAME, "password")
        password_box.send_keys(PASSWORD)
        enter_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        enter_button.click()
        time.sleep(3)
        self.find_followers()

    def find_followers(self):
        find_box = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        find_box.send_keys(SIMILAR_ACCOUNT)
        find_box.send_keys(Keys.ENTER)
        find_box.send_keys(Keys.ENTER)
        # similar = self.driver.find_element(By.XPATH,'// *[ @ id = "f3e6cdf3f93d7d4"] / div')
        # similar.click()
        self.follow()

    def follow(self):
        time.sleep(1)
        pass

bot = InstaFollower()

