import time
import unittest
import random
from selenium.webdriver.remote.webelement import WebElement
import locators as lc
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
            driver.find_element(By.XPATH, "//span[@class='sku_wrapper']")).perform()
        driver.save_screenshot('./Screenshots/image1.jpg')
        image = driver.find_element(By.XPATH, "//img[@title='Alaska Seafood Group']")
        assert image.is_displayed()
        if image.is_displayed():
            print("Image is present")
        else:
            print("Image is not present")

    def test_TC_003(self):
        driver = self.driver
        driver.get(pg.sb_url)
        driver.find_element(By.XPATH, "//img[@title='Alaska Seafood Group']").click()
        delay()
        driver.save_screenshot('./Screenshots/image2.jpg')

    def test_TC_004(self):
        driver = self.driver
        driver.get(pg.sb_url)
        driver.find_element(By.XPATH, "//img[@title='Alaska Seafood Group']").click()
        driver.find_element(By.XPATH, "//button[@aria-label='Zoom in/out']").click()
        driver.find_element(By.XPATH, "//button[@aria-label='Zoom in/out']").click()
        driver.find_element(By.XPATH, "//button[@aria-label='Toggle fullscreen']").click()
        driver.find_element(By.XPATH, "//button[@aria-label='Toggle fullscreen']").click()
        driver.find_element(By.XPATH, "//button[@aria-label='Close (Esc)']").click()
        delay()
        driver.save_screenshot('./Screenshots/image3.jpg')

    def tearDown(self):
        self.driver.quit()
