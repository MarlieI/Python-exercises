#! python3
# 2048.py - my solution to practice project "2048"
# from "Automate The Boring Stuff".
# 2048 is a game where you combine tiles by sliding them using the arrow keys.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://play2048.co')
htmlElem = browser.find_element_by_tag_name('html')

# You can get a fairly high score by repeatedly sliding in an up, right,
# down and left pattern over and over again.
# Using time.sleep() to slow down the movements so you can actually see
# the gameplay.
while True:
    htmlElem.send_keys(Keys.UP)
    time.sleep(0.3)
    htmlElem.send_keys(Keys.RIGHT)
    time.sleep(0.3)
    htmlElem.send_keys(Keys.DOWN)
    time.sleep(0.3)
    htmlElem.send_keys(Keys.LEFT)
    time.sleep(0.3)

# Game over? Simply click "Try again" to let the program continue.
