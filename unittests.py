import locators as lc
import time
import unittest
import random

import page as pg
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
def delay():
    time.sleep(random.randint(1, 5))

class SubscriptionBox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_TC_001(self):
        self.driver.get(pg.sb_url)
        assert 'Alaska Seafood Subscription Box - Custom Seafoods' in self.driver.title

    def test_TC_002(self):
        driver = self.driver
        driver.get(pg.sb_url)
        # Scroll down to the element
        ActionChains(driver).move_to_element(
            driver.find_element(lc.sw)).perform()
        delay()
        driver.save_screenshot('./Screenshots/image1.jpg')
        image = driver.find_element(lc.im_asf)
        if image.is_displayed():
            print("Image is present")
        else:
            print("Image is not present")



    def tearDown(self):
        self.driver.quit()
