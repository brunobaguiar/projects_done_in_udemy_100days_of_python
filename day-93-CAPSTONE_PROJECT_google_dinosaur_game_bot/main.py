import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from PIL import Image
import keyboard

opt = Options()
opt.add_argument('window-size=800,450')
driver = webdriver.Chrome(options=opt)
driver.get("https://chromedino.com/")

# # Images to build machine learning bot
# images_list = [Image.open("cactus_single_small.jpg"),
#                Image.open("cactus_double_small.jpg"),
#                Image.open("cactus_triple_small.jpg"),
#                Image.open("cactus_single_big.jpg"),
#                Image.open("cactus_double_big.jpg"),
#                Image.open("cactus_four_mixed.jpg"),
#                Image.open("bird_middle.jpg"),
#                Image.open("cactus_double_spare.jpg")]

# Start Game
time.sleep(2)
pyautogui.press('space')


# # Check Mouse point x,y position and rgb
# while True: #Start loop
#     print(pyautogui.position())
#     x, y = pyautogui.position()
#     r, g, b = pyautogui.pixel(x, y)
#     print(r, g, b)
#     time.sleep(0.1)


# # Get screenshots to analyse game
# for i in range(500):
#     # full game print
#     pyautogui.screenshot(f"z_ss{i}.jpg", region=(0, 0, 800, 450))
#     # dinosaur + close obstacle print
#     # pyautogui.screenshot(f"z_dino_obst{i}.jpg", region=(100, 330, 300, 80))
#     # # close obstacle print
#     # pyautogui.screenshot(f"z_first_obst{i}.jpg", region=(200, 330, 200, 80))
#     # # point for decision to jump
#     # pyautogui.screenshot(f"z_jump{i}.jpg", region=(200, 355, 10, 2))
#     time.sleep(0.1)
#

# Function to check obstacle in an image, obstacle color (83,83,83)
def find_obstacle(image):
    width, height = image.size
    for x in range(0, width, 3):
        for y in range(0, height, 1):
            r, g, b = image.getpixel((x, y))
            if r == 83 and g == 83 and b == 83:
                return True


# Increment on x to match the increase on speed after each 100 points
x = 200
while not keyboard.is_pressed("q"):
    image1 = pyautogui.screenshot(region=(x, 360, 10, 2))
    if find_obstacle(image1):
        pyautogui.press('space')
        x += 3
