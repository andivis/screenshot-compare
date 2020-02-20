import sys
import os
import time
import logging

from selenium import webdriver

class Selenium:
    def getScreenshot(self, url, fileName, secondsBeforeScreenshot, browser='chrome'):
        self.initialize(browser)

        self.driver.get(url)

        time.sleep(int(secondsBeforeScreenshot))

        self.driver.save_screenshot(fileName)

    def shutdown(self):
        self.driver.quit()

    def initialize(self, browser):
        if self.initialized:
            return

        self.initialized = True

        if browser == 'chrome':
            chromedriver = "chromedriver.exe"
            self.driver = webdriver.Chrome(chromedriver)
        else:
            self.driver = webdriver.Firefox()
    
    def __init__(self):
        self.initialized = False
        self.driver = None
